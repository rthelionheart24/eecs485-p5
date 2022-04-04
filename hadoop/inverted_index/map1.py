#!/usr/bin/env python3
"""Map 1."""
import csv
import re
import sys


with open('stopwords.txt') as file:
    stopwords = set(file.read().split('\n'))

csv.field_size_limit(sys.maxsize)
for row in csv.reader(sys.stdin):
    doc_id, title, body = row
    text = title + " " + body
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    text = text.casefold()
    words = text.split()
    words = [word for word in words if word not in stopwords]
    for word in words:
        print(word, doc_id)
