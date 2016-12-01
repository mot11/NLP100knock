#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

line1 = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. '
         'New Nations Might Also Sign Peace Security Clause. Arthur King Can.')

word = ''
word_list = []
dictionary = {}

for i in range(len(line1)):

    m = re.search('[ .,]', line1[i]) or i + 1 == len(line1)

    if m:

        if i + 1 == len(line1):
            word += line1[i]
        if word != '':
            word_list.append(word)
            word = ''

    else:

        word += line1[i]

for i in range(len(word_list)):

    m = re.search('[0]|[4-8]|1[458]', str(i))

    if m:
        index = word_list[i][0] + word_list[i][1]
    else:
        index = word_list[i][0]

    dictionary[index] = str(i)

print dictionary

