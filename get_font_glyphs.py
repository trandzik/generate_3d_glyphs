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

# chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
# print(list(chars))

# chars = chain.from_iterable([y[0] for y in x.cmap.items()] for x in ttf["cmap"].tables)

chars_unique = []
for char in chars:
    if char not in chars_unique:
        chars_unique.append(char)

with open('glyphs.txt', 'w', encoding='utf8') as f:
    # i = 0
    # line_len = int(len(chars_unique) ** 0.5)
    for char in chars_unique:
        # if i > 0 and i % line_len == 0:
        #     f.write("\n")
        f.write("%s " % char)
        # i += 1

# Use this for just checking if the font contains the codepoint given as
# second argument:
#char = int(sys.argv[2], 0)
#print(Unicode[char])
#print(char in (x[0] for x in chars))

ttf.close()