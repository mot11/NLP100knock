# -*- coding: utf-8 -*-


def merge_list(list_value, list_ref1, a, b, c):
    # merges arrays in list_in at list_in[a..b] and list_in[b+1...c].

    length1 = b - a + 1
    length2 = c - b

    hoge_a = []
    h_ref_1a = []
    hoge_b = []
    h_ref_1b = []

    for ii in range(0, length1):
        hoge_a.append(list_value[a + ii])
        h_ref_1a.append(list_ref1[a + ii])

    for ii in range(0, length2):
        hoge_b.append(list_value[b + 1 + ii])
        h_ref_1b.append(list_ref1[b + 1 + ii])

    # Index of first, second, and merged arrays

    ii = 0
    jj = 0
    k = a

    while ii < length1 and jj < length2:
        if float(hoge_a[ii]) > float(hoge_b[jj]):
            list_value[k] = hoge_a[ii]
            list_ref1[k] = h_ref_1a[ii]
            ii += 1
        else:
            list_value[k] = hoge_b[jj]
            list_ref1[k] = h_ref_1b[jj]
            jj += 1
        k += 1

    while ii < length1:
        list_value[k] = hoge_a[ii]
        list_ref1[k] = h_ref_1a[ii]
        ii += 1
        k += 1

    while jj < length2:
        list_value[k] = hoge_b[jj]
        list_ref1[k] = h_ref_1b[jj]
        jj += 1
        k += 1


def merge_sort(list_value, list_ref1, l, r):
    if l < r:
        m = int((l+r)/2)
        merge_sort(list_value, list_ref1, l, m)
        merge_sort(list_value, list_ref1, m + 1, r)
        merge_list(list_value, list_ref1, l, m, r)


with open('hightemp.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

col1 = []

result = []
nums = []

[col1.append(x[0]) for x in content]

for i in range(len(col1)):
    match = False

    for j in range(len(result)):
        if col1[i] == result[j]:
            nums[j] += 1
            match = True
            break

    if not match:
        result.append(col1[i])
        nums.append(1)


merge_sort(nums, result, 0, len(result)-1)

for i in range(len(nums)):
    print(str(result[i]) + ' ' + str(nums[i]))
