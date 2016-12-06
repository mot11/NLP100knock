#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

line1 = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. '
         'New Nations Might Also Sign Peace Security Clause. Arthur King Can.')

word = ''
dictionary = {}

pa = re.compile('\w+(?=\W)')

word_list = [m.group() for m in pa.finditer(line1)]

for i in range(len(word_list)):

    m = re.search('[0]|[4-8]|1[458]', str(i))

    if m:
        index = word_list[i][0] + word_list[i][1]
    else:
        index = word_list[i][0]

    dictionary[index] = str(i)

print(dictionary)
