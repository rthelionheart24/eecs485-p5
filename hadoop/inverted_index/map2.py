#!/usr/bin/env python3
"""Map 2."""
import sys

for row in sys.stdin:
    term, doc_id = row.split()
    print(f"{term}\t{doc_id}")
