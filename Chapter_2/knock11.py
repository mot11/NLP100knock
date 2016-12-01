# -*- coding: utf-8 -*-

import re

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

content = [re.sub('\t', ' ', x) for x in content]
content = [re.sub('\n', '', x) for x in content]

print(content)