# -*- coding: utf-8 -*-

# merges col1.txt and col2.txt and outputs to mer.txt

with open('col1.txt', 'r', encoding='utf-8') as f:
    col1 = f.readlines()

with open('col2.txt', 'r', encoding='utf-8') as f:
    col2 = f.readlines()

# length of col1[0] and col2[0] are the same by definition.

mer = []

for i in range(len(col1[0])):
    mer.append(col1[0][i] + '\t' + col2[0][i])

print(mer)

with open('mer.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(mer))
    f.close()
