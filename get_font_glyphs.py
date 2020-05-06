#!/usr/bin/env python
from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

ttf = TTFont(sys.argv[1])

chars = []
for cmap in ttf['cmap'].tables:
    if cmap.isUnicode():
        for item in cmap.cmap:
            chars.append(chr(item))

chars_unique = []
for char in chars:
    if char not in chars_unique:
        chars_unique.append(char)

with open('glyphs.txt', 'w', encoding='utf8') as f:
    for char in chars_unique:
        f.write("%s " % char)

# Use this to check if font contains the codepoint given as second argument:
#char = int(sys.argv[2], 0)
#print(Unicode[char])

ttf.close()