#!/usr/bin/env python3
"""Merge multiple CSV files into one."""
import sys, csv, os

def merge(output, *inputs):
    rows = []
    headers = []
    for f in inputs:
        with open(f) as fh:
            r = csv.DictReader(fh)
            if not headers: headers = r.fieldnames
            rows.extend(list(r))
    with open(output, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader()
        w.writerows(rows)
    print(f"✅ Merged {len(inputs)} files → {output} ({len(rows)} rows)")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: csv_merger.py output.csv input1.csv input2.csv ...")
        sys.exit(1)
    merge(sys.argv[1], *sys.argv[2:])
