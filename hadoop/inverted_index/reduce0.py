#!/usr/bin/env python3
"""Reduce 0."""
import sys


def main():
    """Divide sorted lines into groups that share a key."""
    count = 0
    for _ in sys.stdin:
        count += 1
    print(count)


if __name__ == "__main__":
    main()
