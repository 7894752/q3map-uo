#!/usr/bin/env python3
"""Standalone UO q3map.exe build with Visual C++ 7.1 (VS .NET 2003).

Python 3, standard library only. Reads build/sources.json (static manifest: per-TU flag sets, link
order, link options); needs no external project tooling. Never executes the output.

    python build.py --vc7 "C:\\Program Files\\Microsoft Visual Studio .NET 2003\\Vc7"
    python build.py --vc7 <Vc7> --identical      # also write q3map_identical.exe (timestamp/GUID/age stamp)

The VC7 root is the folder that contains bin\\cl.exe, include\\, lib\\ and PlatformSDK\\ (or the
VCINSTALLDIR environment variable of a VS command prompt). --sdk overrides <vc7>\\PlatformSDK
(include\\ and lib\\ of the Platform SDK that provides GL\\glaux.h and glaux.lib).
The pinned February 2003 SDK headers in toolchain_manifest.json are the default.
--sdk-include overrides only those headers, keeping the libraries selected by --sdk.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import threading

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))  # local build modules also work with python -I
ROOT = HERE.parent
MANIFEST = HERE / 'sources.json'

# SHA-256 of the original UO q3map.exe (561,152 bytes, September 2004).
ORIGINAL_SHA256 = 'edf423e0b7607c226bfe26bb591662a098a703a65459b91a53530923933e2fad'

# Verified toolchain files (link 7.10.3077 / cl 13.10.3077). A mismatch is a
# warning (error with --strict): other builds will compile, but are not expected to give identical bytes.
TOOLCHAIN = json.loads((HERE / 'toolchain_manifest.json').read_text(encoding='utf-8'))
EXPECTED = TOOLCHAIN['tools']
EXPECTED_SDK = TOOLCHAIN['sdk']
EXPECTED_GLAUX = TOOLCHAIN['glaux']['sha256']
GLAUX = None

CREATE_NO_WINDOW = (0x08000000 | 0x00004000) if os.name == 'nt' else 0   # no window, below-normal priority
print_lock = threading.Lock()

# Optional Wine mode (experimental, untested by the maintainers): every tool runs as `wine tool.exe ...` and
# every path handed to a tool is converted to a Windows path (`winepath -w`, fallback: Z: drive mapping).
WINE = None        # list such as ['wine'] when active
DRY_RUN = False    # print the commands instead of running them
_wpath_cache = {}


def wpath(p):
    """Path as the tool must see it: unchanged on Windows, Windows-style under Wine."""
    p = str(p)
    if WINE is None:
        return p
    if p in _wpath_cache:
        return _wpath_cache[p]
    if len(p) > 1 and p[1] == ':' and p[0].isalpha():      # already a Windows path
        w = p
    elif DRY_RUN:
        w = 'Z:' + p.replace('/', chr(92))
    else:
        try:
            r = subprocess.run(['winepath', '-w', p], capture_output=True, timeout=60)
            w = r.stdout.decode('utf-8', 'replace').strip() if r.returncode == 0 else ''
        except OSError:
            w = ''
        if not w:
            w = 'Z:' + p.replace('/', chr(92))
    _wpath_cache[p] = w
    return w


def sub(base, name):
    """base/name, resolved case-insensitively (Platform SDK folders are `Include`/`Lib` in some installs)."""
    d = Path(base) / name
    if d.exists() or not Path(base).is_dir():
        return d
    for e in Path(base).iterdir():
        if e.name.lower() == name.lower():
            return e
    return d


def log(*a):
    with print_lock:
        print(*a, flush=True)


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


FETCHED = HERE / 'toolchain' / 'vc7'


def find_vc7(arg):
    if DRY_RUN and arg:
        return Path(arg.strip('"').rstrip(chr(92) + '/'))
    cand = arg or os.environ.get('VCINSTALLDIR')
    if not cand and (FETCHED / 'bin' / 'cl.exe').is_file():
        cand = str(FETCHED)
    if not cand:
        raise SystemExit('Pass --vc7 <path to the genuine VS .NET 2003 Vc7 folder> or set VCINSTALLDIR.')
    p = Path(cand.strip('"').rstrip('\\/'))
    for c in (p, p / 'Vc7'):
        if (c / 'bin' / 'cl.exe').is_file():
            return c.resolve()
    raise SystemExit('No bin\\cl.exe under ' + str(p))


def tool_env(vc7):
    env = os.environ.copy()
    for k in ('CL', '_CL_', 'LINK', '_LINK_', 'INCLUDE', 'LIB', 'LIBPATH'):
        env.pop(k, None)
    extra = [vc7 / 'bin']
    for rel in ('../Common7/IDE', '../Common7/Tools', '../Common7/Tools/bin'):  # mspdb70.dll lives in Common7\IDE
        d = (vc7 / rel).resolve()
        if d.is_dir():
            extra.append(d)
    if WINE is None:
        env['PATH'] = os.pathsep.join([str(d) for d in extra] + [env.get('PATH', '')])
    else:
        # Wine extends the Windows PATH of the prefix from WINEPATH (Windows paths, ';' separated)
        env['WINEPATH'] = ';'.join([wpath(d) for d in extra] + ([env['WINEPATH']] if env.get('WINEPATH') else []))
    return env


def run(cmd, cwd, env, timeout=600):
    """cmd[0] is the tool exe (native path); the other items are already-converted arguments."""
    if WINE is not None:
        tool, args = cmd[0], list(cmd[1:])
        cmd = [*WINE, tool, *args]
        if sum(len(a) + 1 for a in cmd) > 1800:          # long command lines go through a response file
            rsp = Path(cwd) / ('cmd_%d.rsp' % (abs(hash(tuple(args))) % 10**8))
            if not DRY_RUN:
                rsp.write_text(chr(10).join('"' + a + '"' for a in args) + chr(10), encoding='ascii')
            cmd = [*WINE, tool, '@' + wpath(rsp)]
    if DRY_RUN:
        log('DRY-RUN (cwd %s): %s' % (cwd, ' '.join('"%s"' % a if ' ' in a else a for a in cmd)))
        return 0, ''
    r = subprocess.run(cmd, cwd=str(cwd), env=env, capture_output=True, timeout=timeout, creationflags=CREATE_NO_WINDOW)
    return r.returncode, (r.stdout + r.stderr).decode('mbcs' if os.name == 'nt' else 'utf-8', 'replace')


def compile_one(tu, flag_sets, vc7, sdk, out, env, sdk_include=None):
    src = ROOT / tu['source']
    if not DRY_RUN and not src.is_file():
        return tu, 1, 'missing source ' + str(src)
    stem = tu['obj'][:-4]
    work = out / 'work' / stem
    work.mkdir(parents=True, exist_ok=True)
    flags = flag_sets[tu['flags']]
    obj = out / 'obj' / tu['obj']
    # Same include search as the verified build: the TU's own directory, src, then the toolchain.
    header_flags = ['/I' + wpath(sdk_include)] if sdk_include is not None else []
    cmd = [str(vc7 / 'bin' / 'cl.exe'), *flags, *header_flags, '/I' + wpath(src.parent), '/I' + wpath(ROOT / 'src'),
           '/I' + wpath(sub(vc7, 'include')), '/I' + wpath(sub(sdk, 'include')),
           '/Fo' + wpath(obj), '/Fd' + wpath(work / 'compiler.pdb')]
    e = dict(env)
    if '/YX' in flags:
        cmd.append('/Fp' + wpath(work / 'auto.pch'))   # private PCH per TU, deleted afterwards
    else:
        e['TMP'] = e['TEMP'] = wpath(work)             # cl.exe hangs with /YX under a TMP override
    cmd.append(wpath(src))
    code, text = run(cmd, work, e)
    if DRY_RUN:
        return tu, 0, ''
    (work / 'compile.log').write_text(text, encoding='utf-8')
    for junk in ('auto.pch', 'compiler.pdb'):
        try:
            (work / junk).unlink()
        except OSError:
            pass
    return tu, code if obj.exists() else (code or 1), text


def compile_all(man, vc7, sdk, out, env, jobs, keep_going, sdk_include=None):
    (out / 'obj').mkdir(parents=True, exist_ok=True)
    tus = man['translation_units']
    failed = []
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as ex:
        futs = [ex.submit(compile_one, tu, man['compile_flag_sets'], vc7, sdk, out, env, sdk_include) for tu in tus]
        for f in concurrent.futures.as_completed(futs):
            tu, code, text = f.result()
            done += 1
            if code:
                failed.append(tu['source'])
                log('FAILED  [%d/%d] %s\n%s' % (done, len(tus), tu['source'], text))
                if not keep_going:
                    for g in futs:
                        g.cancel()
                    break
            else:
                log('compiled [%d/%d] %s (%s)' % (done, len(tus), tu['source'], tu['flags']))
    return failed


def link_all(man, vc7, sdk, out, env, pdbaltpath, objdir=None):
    obj = Path(objdir) if objdir else out / 'obj'

    # --- the original solution built jpeg-6 (+jpgload), cmdlib and NvTriStrip as static libraries; the linker
    # pulls their members in reference order, which gives the original object order.
    libdir = out / 'lib'
    libdir.mkdir(parents=True, exist_ok=True)
    libpath = {}
    for name, members in man['static_libraries'].items():
        lib = libdir / (name + '.lib')
        if lib.exists():
            lib.unlink()
        code, text = run([str(vc7 / 'bin' / 'lib.exe'), '/NOLOGO', '/OUT:' + wpath(lib), *[wpath(obj / m) for m in members]],
                         libdir, env)
        if code:
            raise SystemExit('lib.exe failed for %s:%s%s' % (name, chr(10), text))
        libpath['@' + name] = wpath(lib)

    flags = list(man['link_flags'])
    flags += ['/PDB:' + wpath(out / 'q3map.pdb'), '/OUT:' + wpath(out / 'q3map.exe'), '/MAP:' + wpath(out / 'q3map.map'),
              '/LIBPATH:' + wpath(sub(vc7, 'lib')), '/LIBPATH:' + wpath(sub(sdk, 'lib'))]
    flags = [f for f in flags if not f.startswith('/PDBALTPATH:')]
    if pdbaltpath:
        flags.append('/PDBALTPATH:' + pdbaltpath)
    flags += ['/INCLUDE:' + s for s in man.get('link_include_roots', [])]
    inputs = [wpath(obj / t['obj']) for t in man['translation_units'] if t['project'] == 'q3map']
    # Explicit library paths in the manifest are relative to the project root;
    # bare names retain the normal toolchain/SDK library search.
    libs = [wpath(GLAUX) if l == '@glaux' else libpath[l] if l in libpath else wpath(ROOT / l) if '/' in l or chr(92) in l else l
            for l in man['link_libraries']]
    rsp = out / 'q3map.rsp'
    rsp.write_text('\n'.join('"' + a + '"' for a in flags + inputs + libs) + '\n', encoding='ascii')
    code, text = run([str(vc7 / 'bin' / 'link.exe'), '@' + wpath(rsp)], out, env)
    if DRY_RUN:
        return out / 'q3map.exe'
    (out / 'link.log').write_text(text, encoding='utf-8')
    if code:
        print(text)
        raise SystemExit('link.exe failed (exit %d)' % code)
    return out / 'q3map.exe'


def check_toolchain(vc7, sdk, strict, sdk_include=None, sdk_headers=None):
    bad = []
    for base, table in ((vc7, EXPECTED), (sdk, EXPECTED_SDK)):
        for rel, want in table.items():
            p = base / rel
            if not p.is_file():
                bad.append('missing  ' + str(p))
            elif sha256(p) != want:
                bad.append('differs  ' + str(p))
    if sdk_include is not None and sdk_headers is not None:
        for rel, want in sdk_headers['files'].items():
            p = sdk_include / rel
            if not p.is_file():
                bad.append('missing  ' + str(p))
            elif sha256(p) != want:
                bad.append('differs  ' + str(p))
    if not GLAUX.is_file() or sha256(GLAUX) != EXPECTED_GLAUX:
        bad.append('missing or differing GlAux archive: ' + str(GLAUX))
    if bad:
        log('WARNING: toolchain files differ from the verified VS .NET 2003 (13.10.3077 / 7.10.3077) install:')
        for b in bad:
            log('   ' + b)
        if strict:
            raise SystemExit('--strict: toolchain mismatch')
    else:
        log('toolchain: all verified files match')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--vc7', help='Vc7 root (contains bin\\cl.exe); default: %%VCINSTALLDIR%%')
    ap.add_argument('--sdk', help='Platform SDK root (include\\, lib\\); default <vc7>\\PlatformSDK')
    ap.add_argument('--sdk-include', help='override pinned February 2003 SDK headers; --sdk still selects libraries')
    ap.add_argument('--out', default=str(HERE / 'out'), help='output directory (default build\\out)')
    ap.add_argument('--identical', action='store_true',
                    help='also write q3map_identical.exe with the original timestamp and RSDS GUID/age')
    ap.add_argument('--fetch-toolchain', action='store_true',
                    help='fetch pinned VC7.1, February 2003 headers and August 2002 GlAux (needs 7-Zip)')
    ap.add_argument('--sdk-include-source', help='extracted February 2003 SDK Include directory for --fetch-toolchain')
    ap.add_argument('--7z', dest='sevenzip', help=argparse.SUPPRESS)
    ap.add_argument('--keep-downloads', action='store_true', help=argparse.SUPPRESS)
    ap.add_argument('--jobs', type=int, default=1, choices=[1], help='compiler processes (1)')
    ap.add_argument('--keep-going', action='store_true', help='continue after a failed compile')
    ap.add_argument('--strict', action='store_true', help='fail if toolchain file hashes differ from the verified install')
    ap.add_argument('--link-only', action='store_true', help='reuse the objects already in <out>\\obj')
    ap.add_argument('--clean', action='store_true', help='delete <out> first')
    ap.add_argument('--wine', nargs='?', const='wine', default=None, metavar='WINE_CMD',
                    help='EXPERIMENTAL (untested): run the VC7 tools under Wine (default command "wine"); '
                         'enabled automatically when not on Windows')
    ap.add_argument('--dry-run', action='store_true',
                    help='print the tool command lines (after path conversion) without running anything')
    ap.add_argument('--glaux', help='pinned August 2002 GlAux archive; defaults to build/toolchain/link_inputs/glaux_aug2002.lib')
    ap.add_argument('--original', type=Path, help='read a supplied reference for complete byte/section diagnostics')
    ap.add_argument('--require-identical', action='store_true', help='exit 3 unless the result equals the recorded reference hash')
    args = ap.parse_args()
    if args.original and not args.dry_run:
        if not args.original.is_file():
            ap.error('reference image not found: ' + str(args.original))
        if args.strict and sha256(args.original) != ORIGINAL_SHA256:
            ap.error('supplied reference does not match the recorded UO q3map SHA-256')
    global WINE, DRY_RUN, GLAUX
    DRY_RUN = args.dry_run
    if args.wine is None and os.name != 'nt':
        args.wine = 'wine'
        log('Not running on Windows: using Wine to run the VC7 tools (experimental, untested; see build/README.md).')
    if args.wine is not None:
        import shlex
        WINE = shlex.split(args.wine)

    man = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if args.fetch_toolchain:
        import fetch_toolchain
        fetch_args = ['--sdk-include-source', args.sdk_include_source] if args.sdk_include_source else []
        if args.sevenzip:
            fetch_args += ['--7z', args.sevenzip]
        if args.keep_downloads:
            fetch_args += ['--keep']
        if fetch_toolchain.main(fetch_args):
            raise SystemExit('toolchain fetch failed')
        if not args.vc7:
            args.vc7 = str(FETCHED)
    vc7 = find_vc7(args.vc7)
    sdk = Path(args.sdk).resolve() if args.sdk else sub(vc7, 'PlatformSDK')
    sdk_headers = None
    if man.get('toolchain_manifest'):
        sdk_headers = json.loads((ROOT / man['toolchain_manifest']).read_text(encoding='utf-8'))['sdk_headers']
    sdk_include = Path(args.sdk_include).resolve() if args.sdk_include else (ROOT / sdk_headers['path']).resolve() if sdk_headers else None
    if not DRY_RUN and sdk_include is not None and not sdk_include.is_dir():
        raise SystemExit('SDK header directory not found: ' + str(sdk_include)
                         + '; stage it with --fetch-toolchain --sdk-include-source <Microsoft SDK Include directory>.')
    if not DRY_RUN and (not sub(sdk, 'lib').is_dir() or not sub(sdk, 'include').is_dir()):
        raise SystemExit('Platform SDK include\\ and lib\\ not found under ' + str(sdk) + ' (use --sdk)')
    GLAUX = Path(args.glaux).resolve() if args.glaux else HERE / 'toolchain/link_inputs/glaux_aug2002.lib'
    out = Path(args.out).resolve()
    if args.original:
        reference_path = args.original.resolve()
        if reference_path in {out / 'q3map.exe', out / 'q3map_identical.exe'} or (args.clean and out in reference_path.parents):
            ap.error('output/clean operation would overwrite or remove the reference image')
    if args.clean and out.exists():
        build_root = HERE.resolve()
        if build_root not in out.parents or out.is_symlink():
            raise SystemExit('--clean only accepts an output directory below build/')
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)
    log('VC7   :', vc7)
    log('SDK   :', sdk)
    if sdk_include is not None:
        log('headers:', sdk_include)
    log('output:', out)
    if not DRY_RUN:
        check_toolchain(vc7, sdk, args.strict, sdk_include, sdk_headers)
    env = tool_env(vc7)

    if not args.link_only:
        failed = compile_all(man, vc7, sdk, out, env, max(1, min(args.jobs, 2)), args.keep_going, sdk_include)
        if failed:
            raise SystemExit('%d translation unit(s) failed: %s' % (len(failed), ', '.join(failed)))
    exe = link_all(man, vc7, sdk, out, env, r'c:\Cod\bin\q3map.pdb')
    if DRY_RUN:
        log('dry run finished: no tool was executed')
        return 0
    result = exe
    log('linked', exe)
    if args.identical:
        import stamp_meta
        result = out / 'q3map_identical.exe'
        result.write_bytes(stamp_meta.apply_policy(exe.read_bytes(),
                                                   json.loads((HERE / 'meta_stamp.json').read_text(encoding='utf-8'))))
        log('stamped', result)
    digest = sha256(result)
    log('')
    log('sha256 ', digest)
    log('original', ORIGINAL_SHA256)
    if args.original:
        import compare_image
        comparison = compare_image.compare_files(args.original, result)
        report = out / 'diff_report.json'
        compare_image.write_report(comparison, report, (args.original, result))
        log('different file bytes:', comparison['differing_bytes'])
        log('header bytes:', comparison['header_differing_bytes'])
        for section in comparison['sections']:
            log(section['name'] + ':', section['differing_bytes'])
        log('comparison report:', report)
    if digest == ORIGINAL_SHA256:
        log('RESULT: IDENTICAL to the original q3map.exe')
        return 0
    log('RESULT: differs from the original q3map.exe (without --identical the timestamp, PDB GUID and age differ by design; see build\\README.md)')
    return 3 if args.require_identical else 0


if __name__ == '__main__':
    sys.exit(main())
