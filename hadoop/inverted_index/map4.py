#!/usr/bin/env python3
"""Map 4."""
import sys

for row in sys.stdin:
    term, idf, doc_id, tf, norm_factor = row.split()
    key = int(doc_id) % 3
    print(f"{key}\t{term}\t{doc_id}\t{idf} {tf} {norm_factor}")
