#!/usr/bin/env python3
"""Map 0."""
import csv
import sys

csv.field_size_limit(sys.maxsize)
for _ in csv.reader(sys.stdin):
    print()
