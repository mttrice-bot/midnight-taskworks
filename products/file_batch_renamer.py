#!/usr/bin/env python3
"""Batch rename files with patterns."""
import os, sys, re

def rename(directory, pattern, replacement, dry_run=True):
    changed = 0
    for f in os.listdir(directory):
        if pattern in f:
            new = f.replace(pattern, replacement)
            print(f"  {f} → {new}")
            if not dry_run:
                os.rename(os.path.join(directory, f), os.path.join(directory, new))
            changed += 1
    print(f"\n{'🔍 DRY RUN' if dry_run else '✅ DONE'}: {changed} files")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: file_renamer.py <dir> <pattern> <replacement> [--run]")
        sys.exit(1)
    dry = "--run" not in sys.argv
    rename(sys.argv[1], sys.argv[2], sys.argv[3], dry_run=dry)
