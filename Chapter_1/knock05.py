# -*- coding: utf-8 -*-

import re


def ngram_make(n, li):
    # type: (int, list) -> list

    output_list = []

    for i in range(len(li)):

        ngram = ''

        if i + n <= len(li):

            for j in range(n):
                if j == 0:
                    ngram = li[i + j]
                else:
                    ngram += ' ' + li[i + j]
            output_list.append(ngram)

    return output_list


def split_words(line):
    # type: (str) -> list
    split_done = re.sub('[^\w]', ' ', line).split()
    return split_done


def split_letters(line):
    # type: (str) -> list
    split_done = re.sub('[^\w]', '', line)
    return split_done


size_of_ngram = int(input('Input size of n-gram.\n'))

line1 = 'I am an NLPer'

line_sw = split_words(line1)
line_sl = split_letters(line1)

output_sw = ngram_make(size_of_ngram, line_sw)
output_sl = ngram_make(size_of_ngram, line_sl)

print('N-gram of words is: ', output_sw)
print('N-gram of letters is: ', output_sl)
