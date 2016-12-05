# -*- coding: utf-8 -*-

import re


def find_section(str_1):
    p = re.compile(r'=+[\w]+=+', re.IGNORECASE)
    category = []
    for m in p.finditer(str_1):
        category.append(m.group())
    return category

with open('uk.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

sec = find_section(content[0])

pp = re.compile(r'=')

for x in sec:
    count = 0
    for m in pp.finditer(x):
        count += 1

    count = count / 2 - 1

    print(x, int(count))