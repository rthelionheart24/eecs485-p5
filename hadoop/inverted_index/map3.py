#!/usr/bin/env python3
"""Map 3."""
import sys

for row in sys.stdin:
    doc_id, term, idf, tf = row.split()
    print(f"{doc_id}\t{term} {idf} {tf}")
