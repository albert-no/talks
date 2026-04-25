#!/usr/bin/env python3
"""Find prose blocks (p, li) with high word counts across deck files.

Usage: python scripts/find-wordy.py mia/*.html
"""
import re, sys, pathlib

THRESHOLD_P = 16   # words per <p>
THRESHOLD_LI = 14  # words per <li>

def count_words(html):
    text = re.sub(r'<[^>]+>', '', html)
    text = re.sub(r'\$[^$]*\$', 'X', text)  # treat each $...$ as one token
    return len(text.split()), text.strip()

for path in sys.argv[1:]:
    p = pathlib.Path(path)
    src = p.read_text(encoding='utf-8')
    print(f'=== {path} ===')

    for tag, threshold in (('p', THRESHOLD_P), ('li', THRESHOLD_LI)):
        pattern = re.compile(rf'<{tag}\b[^>]*>(.*?)</{tag}>', re.DOTALL)
        for m in pattern.finditer(src):
            wc, text = count_words(m.group(1))
            if wc >= threshold:
                line = src[:m.start()].count('\n') + 1
                snippet = text[:160].replace('\n', ' ')
                print(f'  L{line} <{tag}> ({wc}w): {snippet}')
    print()
