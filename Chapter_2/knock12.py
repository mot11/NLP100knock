# -*- coding: utf-8 -*-

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

out_1 = []
out_2 = []

[out_1.append(x[0]) for x in content]
[out_2.append(x[1]) for x in content]

print(out_1)
print(out_2)

with open('col1.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(out_1))
    f.close()

with open('col2.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(out_2))
    f.close()

print('Files written.')