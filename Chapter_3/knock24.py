# -*- coding: utf-8 -*-

import re


def find_files(str_1):

    p = re.compile(r'(?<=(File:))[^|]+(?=|)')

    output = [m.group() for m in p.finditer(str_1)]

    return output

with open('uk.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

file_ref = find_files(content[0])

print('\n'.join(file_ref))
