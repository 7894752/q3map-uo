"""Read-only PE32 byte comparison. Images are read as data and never executed."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import struct


def pe_layout(data):
    if len(data) < 64 or data[:2] != b'MZ':
        raise ValueError('input is not a complete DOS/PE image')
    pe = struct.unpack_from('<I', data, 60)[0]
    if pe > len(data) - 24 or data[pe:pe + 4] != b'PE\0\0':
        raise ValueError('missing or truncated PE header')
    opt = pe + 24
    opt_size = struct.unpack_from('<H', data, pe + 20)[0]
    count = struct.unpack_from('<H', data, pe + 6)[0]
    if opt_size < 64 or opt + opt_size + count * 40 > len(data):
        raise ValueError('truncated optional header or section table')
    if struct.unpack_from('<H', data, opt)[0] != 0x10b:
        raise ValueError('expected a PE32 image')
    header_size = struct.unpack_from('<I', data, opt + 60)[0]
    if header_size > len(data):
        raise ValueError('header size exceeds the file size')
    sections = []
    names = set()
    for i in range(count):
        off = opt + opt_size + i * 40
        name = data[off:off + 8].rstrip(b'\0').decode('ascii', errors='replace')
        virtual_size, rva, raw_size, raw_offset = struct.unpack_from('<IIII', data, off + 8)
        if raw_size and (raw_offset > len(data) or raw_size > len(data) - raw_offset):
            raise ValueError('section raw extent exceeds the file size: ' + name)
        if name in names:
            raise ValueError('duplicate section name: ' + name)
        names.add(name)
        sections.append(dict(name=name, virtual_size=virtual_size, rva=rva,
                             raw_size=raw_size, offset=raw_offset))
    return header_size, sections


def different_bytes(a, b):
    return sum(x != y for x, y in zip(a, b)) + abs(len(a) - len(b))


def compare_bytes(original, candidate):
    original_headers, original_sections = pe_layout(original)
    candidate_headers, candidate_sections = pe_layout(candidate)
    other = {s['name']: s for s in candidate_sections}
    sections = []
    for a in original_sections:
        b = other.pop(a['name'], None)
        x = original[a['offset']:a['offset'] + a['raw_size']]
        y = candidate[b['offset']:b['offset'] + b['raw_size']] if b else b''
        sections.append(dict(name=a['name'], original=a, candidate=b,
                             layout_equal=a == b, differing_bytes=different_bytes(x, y)))
    for b in other.values():
        sections.append(dict(name=b['name'], original=None, candidate=b,
                             layout_equal=False, differing_bytes=b['raw_size']))
    ranges = []
    i = 0
    length = max(len(original), len(candidate))
    boundaries = {s['offset'] for s in original_sections}
    boundaries.update(s['offset'] + s['raw_size'] for s in original_sections)
    while i < length:
        if i < len(original) and i < len(candidate) and original[i] == candidate[i]:
            i += 1
            continue
        start = i
        i += 1
        while i < length and i not in boundaries and (
                i >= len(original) or i >= len(candidate) or original[i] != candidate[i]):
            i += 1
        section = next((s['name'] for s in original_sections
                        if s['offset'] <= start < s['offset'] + s['raw_size']), 'headers/overlay')
        ranges.append(dict(offset=start, end=i, length=i - start, section=section))
    return dict(original_size=len(original), candidate_size=len(candidate),
                original_sha256=hashlib.sha256(original).hexdigest(),
                candidate_sha256=hashlib.sha256(candidate).hexdigest(),
                identical=original == candidate, differing_bytes=different_bytes(original, candidate),
                header_differing_bytes=different_bytes(original[:original_headers], candidate[:candidate_headers]),
                sections=sections, range_count=len(ranges), ranges=ranges)


def compare_files(original, candidate):
    return compare_bytes(Path(original).read_bytes(), Path(candidate).read_bytes())


def write_report(result, report, inputs=()):
    report = Path(report).resolve()
    if report in {Path(p).resolve() for p in inputs}:
        raise ValueError('report path must differ from the input images')
    report.parent.mkdir(parents=True, exist_ok=True)
    with report.open('w', encoding='utf-8', newline='\n') as stream:
        stream.write(json.dumps(result, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original', required=True, type=Path)
    parser.add_argument('--candidate', required=True, type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    try:
        result = compare_files(args.original, args.candidate)
        if args.report:
            write_report(result, args.report, (args.original, args.candidate))
    except (OSError, ValueError, struct.error) as error:
        parser.error(str(error))
    print('IDENTICAL' if result['identical'] else 'DIFFERENT')
    print('different file bytes:', result['differing_bytes'])
    print('header bytes:', result['header_differing_bytes'])
    for section in result['sections']:
        print(section['name'] + ':', section['differing_bytes'])
    print('candidate sha256:', result['candidate_sha256'])
    return 0 if result['identical'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
