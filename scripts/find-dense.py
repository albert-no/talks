#!/usr/bin/env python3
"""Find dense slides (high word count, many bullets, many paragraphs)."""
import re, pathlib, sys

WORD_THRESHOLD = 80
LI_THRESHOLD = 6
P_THRESHOLD = 6

def find_slides(src):
    """Yield (start_line, label, body) for each .slide div."""
    # Naive but works for this codebase: split on opening <div class="slide
    parts = re.split(r'(<div class="slide[^"]*"[^>]*>)', src)
    pos = 0
    for i in range(1, len(parts), 2):
        opener = parts[i]
        body_with_tail = parts[i+1] if i+1 < len(parts) else ''
        depth = 1
        idx = 0
        while idx < len(body_with_tail) and depth > 0:
            mo = re.search(r'<div\b|</div>', body_with_tail[idx:])
            if not mo: break
            tok = mo.group(0)
            idx += mo.end()
            depth += 1 if tok == '<div' else -1
        body = body_with_tail[:idx-len('</div>')] if depth == 0 else body_with_tail
        before = ''.join(parts[:i]) + opener
        line = before.count('\n') + 1
        label_m = re.search(r'data-screen-label="([^"]+)"', opener)
        label = label_m.group(1) if label_m else '?'
        yield line, label, body

for path in sys.argv[1:]:
    src = pathlib.Path(path).read_text(encoding='utf-8')
    print(f'=== {path} ===')
    for line, label, body in find_slides(src):
        text = re.sub(r'<[^>]+>', ' ', body)
        text = re.sub(r'\$[^$]*\$', 'X', text)
        wc = len(text.split())
        li_count = len(re.findall(r'<li\b', body))
        p_count = len(re.findall(r'<p\b', body))
        if wc > WORD_THRESHOLD or li_count > LI_THRESHOLD or p_count > P_THRESHOLD:
            print(f'  L{line} [{label}]  words={wc}  li={li_count}  p={p_count}')
    print()
