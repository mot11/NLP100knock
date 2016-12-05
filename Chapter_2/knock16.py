# -*- coding: utf-8 -*-

file_name = input('Please input the name of a file.\n')

if file_name == '':
    file_name = 'hightemp.txt'

input_number = int(input('Please input an integer.\n'))

with open(file_name, 'r', encoding='utf-8') as f:
    content = f.readlines()

output = []
ticker = 1
a = len(content) / input_number

for i in range(len(content)):
    output.append(content[i])
    if i + 2 > ticker * a:
        ticker += 1
        output.append('\n')

print('Displaying', file_name, 'divided into', input_number, 'parts.')
print(''.join(output))
