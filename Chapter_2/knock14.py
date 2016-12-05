# -*- coding: utf-8 -*-

file_name = input('Please input the name of a file.\n')
input_number = int(input('Please input an integer.\n'))

output = []

with open(file_name, 'r', encoding='utf-8') as f:
    for i in range(input_number):
        output.append(f.readline())

print('Displaying', input_number, 'lines from the beginning of', file_name, ':')
print(''.join(output))
