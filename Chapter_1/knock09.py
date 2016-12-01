# -*- coding: utf-8 -*-

import re
from random import shuffle


def split_words(line):
    # output = re.sub(r' ', ' ', line).split()
    output = line.split()
    return output


def scramble(list_input):
    output = list_input

    p = re.compile(r'[\w\'][\w\']{3,}[\w\']')

    for i in range(len(list_input)):

        m = p.match(list_input[i])

        if m is not None:
            word = m.group()
            print(word, ' -> ', end='')
            hoge = word[1:len(word) - 1]
            h_list = list(hoge)
            shuffle(h_list)
            word = "{0}{1}{2}".format(word[0], ''.join(h_list), word[len(word) - 1])
            print(word)

            output[i] = word

    return ' '.join(output)


input_line = input('Please input an English sentence.\n')

# line1 = input_line.decode('utf-8')
line1 = input_line

if line1 == '':
    line1 = ("I couldn't believe that I could actually understand what I was reading :"
             " the phenomenal power of the human mind .")
    print(line1)

split_line = split_words(line1)
scramble_line = scramble(split_line)

print(scramble_line)
