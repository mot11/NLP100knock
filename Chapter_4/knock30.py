# -*- coding: utf-8 -*-

import re

with open('neko.txt.mecab', 'r', encoding='utf-8') as f:
    content = f.readlines()

# 一行ごとの辞書のリストを作る。
# [[{表層形, 基本形, 品詞, 品詞細分類1},{...},...],[...],...]

neko_morphemes = []
line_morphemes = []

p = re.compile('([^\t]*)\t([^,]*),([^,]*),[^,]*,[^,]*,[^,]*,[^,]*,([^,]*),[^,]*,[^\n]*\n')

for line in content:
    m = p.match(line)
    if m:
        morpheme = {'表層形': m.group(1), '基本形': m.group(4), '品詞': m.group(2), '品詞細分類1': m.group(3)}
        if morpheme['品詞細分類1'] == '句点' or morpheme['品詞細分類1'] == '空白':
            neko_morphemes.append(line_morphemes.copy())
            del line_morphemes[:]
            morpheme.clear()
        elif morpheme['品詞'] != '記号':
            line_morphemes.append(morpheme.copy())
            morpheme.clear()

