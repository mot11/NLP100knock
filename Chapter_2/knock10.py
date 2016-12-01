# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

print('Number of lines:', len(content))
