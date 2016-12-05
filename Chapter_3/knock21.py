# -*- coding: utf-8 -*-

import re


def find_category(str_1):
    p = re.compile(r'(?=(\\n)*)[^(\\n)]*Category[^(\\n)"]*(?=([(\\n)"]))', re.IGNORECASE)
    category = []
    for m in p.finditer(str_1):
        category.append(m.group())
    return category

with open('uk.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

cat = find_category(content[0])
print('\n'.join(cat))
