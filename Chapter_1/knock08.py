# -*- coding: utf-8 -*-

import re

def cipher(line):
    output_line = ''

    for i in range(len(line)):
        m = re.match(r'[a-z]', line[i])
        if m:
            output_line += str(219 - ord(line[i]))
        else:
            output_line += line[i]

    return output_line

def decipher(line):
    output_line = ''
    previous_match = 0
    p = re.compile(r'9[7-9]|1[01][0-9]|12[0-2]')

    for m in p.finditer(line):

        output_line += line[previous_match:m.start()] + chr(219 - int(m.group()))
        previous_match = m.end()

    output_line += line[previous_match:]

    return output_line

input_line_u = input('Please input a message.\n')

c = cipher(input_line_u)
d = decipher(c)

print('Encrypted message is', c)
print('Decrypted message is', d)

