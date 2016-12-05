# -*- coding: utf-8 -*-

import re

# creates text file "uk.txt" from JSON

p = re.compile(r'"イギリス"')

found = False
i = 0

with open('jawiki-country.json', 'r', encoding='utf-8') as f:
    for line in f:
        i += 1

        for m in p.finditer(line):
            found = True
            break

        if found:
            break

with open('uk.txt', 'w', encoding='utf-8') as f:
    f.write(line)
    f.close()

