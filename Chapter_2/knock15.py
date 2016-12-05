# -*- coding: utf-8 -*-

file_name = input('Please input the name of a file.\n')
input_number = int(input('Please input an integer.\n'))

content = []
output = []

with open(file_name, 'r', encoding='utf-8') as f:
    content = f.readlines()

for i in range(len(content)-input_number, len(content)):
    output.append(content[i])

print('Displaying', input_number, 'lines at the end of', file_name, ':')
print(''.join(output))
