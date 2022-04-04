#!/usr/bin/env python3
"""Reduce2."""
import itertools
import sys


def reduce_one_group(key, group):
    """Reduce one group."""
    group = list(group)
    for line in group:
        print(line)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.split()[2]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
