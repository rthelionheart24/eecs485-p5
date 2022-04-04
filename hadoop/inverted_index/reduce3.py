#!/usr/bin/env python3
"""Reduce 3."""
import itertools
import sys


def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    norm_factor = 0
    for line in group:
        _, _, idf, tf = line.split()
        norm_factor += (float(tf) * float(idf)) ** 2
    for line in group:
        _, term, idf, tf = line.split()
        print(term, idf, key, tf, norm_factor)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split()[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
