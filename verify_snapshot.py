#!/usr/bin/env python3
"""Verify a clean release snapshot without importing project/private code."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'EXPORT_MANIFEST.json').read_text())
    expected = manifest['files']
    for name, digest in expected.items():
        path = root / name
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError('Unsafe snapshot path: ' + name)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('Changed or missing snapshot file: ' + name)
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*')
              if p.is_file() and '.git' not in p.relative_to(root).parts}
    if actual != set(expected) | {'EXPORT_MANIFEST.json'}:
        raise ValueError('Unexpected snapshot files: ' + repr(sorted(actual - set(expected))))
    print(f"PASS: {len(expected)} files; atlas {manifest['atlas_build']}; "
          f"statistical release {manifest['statistical_release']}")


if __name__ == '__main__':
    main()
