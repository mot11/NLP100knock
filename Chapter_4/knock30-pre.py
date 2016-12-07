# -*- coding: utf-8 -*-
# Requires installation of MeCab
# Creates neko.txt.mecab

import MeCab

with open('neko.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

m = MeCab.Tagger("")

with open('neko.txt.mecab', 'w', encoding='utf-8') as f:
    f.write(m.parse('\n'.join(content)))
    f.close()
