# -*- coding: utf-8 -*-

import re


def merge_list(a, b, c, col_num):
    # merges arrays in list_in at list_in[a..b] and list_in[b+1...c].

    length1 = b - a + 1
    length2 = c - b

    hoge1 = []
    hoge2 = []

    for i in range(0, length1):
        hoge1.append(list_in[a + i])

    for i in range(0, length2):
        hoge2.append(list_in[b+1 + i])

    # Index of first, second, and merged arrays

    i = 0
    j = 0
    k = a

    while i < length1 and j < length2:
        if float(hoge1[i][col_num-1]) < float(hoge2[j][col_num-1]):
            list_in[k] = hoge1[i]
            i += 1
        else:
            list_in[k] = hoge2[j]
            j += 1
        k += 1

    while i < length1:
        list_in[k] = hoge1[i]
        i += 1
        k += 1

    while j < length2:
        list_in[k] = hoge2[j]
        j += 1
        k += 1


def merge_sort(l, r, col_num):
    if l < r:
        m = int((l+r)/2)
        merge_sort(l, m, col_num)
        merge_sort(m+1, r, col_num)
        merge_list(l, m, r, col_num)


def tab_split(list_1):
    list_out = []
    for x in range(len(list_1)):
        row_list = re.split(r'[\t\n]', list_1[x])
        list_out.append(row_list)
    return list_out


def tab_desplit(list_1):
    list_out = []
    for x in range(len(list_1)):
        row = '\t'.join(list_1[x])
        list_out.append(row)
    return list_out

with open('hightemp.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

content_split = tab_split(content)
list_in = content_split[:]

merge_sort(0, len(content_split)-1, 3)

result_desplit = tab_desplit(list_in)

print('Result:')
print('\n'.join(result_desplit))
