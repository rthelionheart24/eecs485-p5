#!/usr/bin/env python3
"""Reduce 4."""
import itertools
import sys


def reduce_one_group(key, group):
    """Reduce one group."""
    docs = []
    idf = None
    for line in group:
        _, _, doc_id, idf, tf, norm_factor = line.split()
        docs.extend((doc_id, tf, norm_factor))
    print(key, idf, " ".join(docs))


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split()[1]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
