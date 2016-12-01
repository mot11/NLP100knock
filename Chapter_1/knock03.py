#!/usr/bin/env python
# -*- coding: utf-8 -*-

line1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

length = len(line1)
word = ''
word_list = []
word_number = 0
letter_list_1 = []
letter_list_2 = []
new_letter = True
letters = 0


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


for i in range(length):

    if line1[i] == ' ' or line1[i] == ',' or line1[i] == '.':
        if word != '':
            word_list.append(word)
            word = ''
    else:
        word += line1[i]

print('Words:')
print('')

for i in range(len(word_list)):
    word = word_list[i]
    print(word)

    for j in range(len(word)):
        new_letter = True

        for k in range(len(letter_list_1)):
            if letter_list_1[k] == word[j].upper():
                letter_list_2[k] += 1
                new_letter = False
                break

        if new_letter:
            letter_list_1.append(word[j].upper())
            letter_list_2.append(1)

    for j in range(len(letter_list_1)):
        print(letter_list_1[j] + ' = ' + str(letter_list_2[j]))

    del letter_list_1[:]
    del letter_list_2[:]
    print('')
