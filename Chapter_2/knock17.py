# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

col1 = []

for i in range(len(content)):
    noMatch = True

    for j in range(len(col1)):
        if content[i][0] == col1[j]:
            noMatch = False
            break

    if noMatch:
        col1.append(content[i][0])

output = ''.join(col1)

print(output)
