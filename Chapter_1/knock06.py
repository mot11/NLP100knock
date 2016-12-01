# -*- coding: utf-8 -*-

def ngram_make(n, li):

    output_list = []

    for i in range(len(li)):

        ngram = ''

        if i + n <= len(li):

            for j in range(n):
                if j == 0:
                    ngram = li[i + j]
                else:
                    ngram += li[i + j]

            isalreadythere = False

            for k in range(len(output_list)):
                if output_list[k] == ngram:
                    isalreadythere = True

            if not isalreadythere:
                output_list.append(ngram)

    return output_list

def set_union(li1, li2):

    output_list = li1[:]

    for i in range(len(li2)):
        isalreadythere = False

        for j in range(len(li1)):
            if li1[j] == li2[i]:
                isalreadythere = True

        if not isalreadythere:
            output_list.append(li2[i])

    return output_list

def set_intersection(li1, li2):

    output_list = []

    for i in range(len(li1)):

        for j in range(len(li2)):
            if li1[i] == li2[j]:
                output_list.append(li1[i])
                break

    return output_list

def set_complement(li1, li2):

    output_list = []

    for i in range(len(li2)):
        isthere = False
        for j in range(len(li1)):
            if li1[j] == li2[i]:
                isthere = True
                break

        if not isthere:
            output_list.append(li2[i])

    return output_list

word_1 = 'paraparaparadise'
word_2 = 'paragraph'

X = ngram_make(2, word_1)
Y = ngram_make(2, word_2)

print(X)
print(Y)

print('Union is ', set_union(X, Y), '')
print('Intersection is ', set_intersection(X, Y), '')
print('Complement of set X with respect to Y is', set_complement(X, Y), '')
print('Complement of set Y with respect to X is', set_complement(Y, X), '')

for i in range(len(X)):
    if X[i] == 'se':
        print('\'se\' was contained in X.')
        break
    if i+1 == len(X):
        print('\'se\' was not contained in X.')

for i in range(len(Y)):
    if Y[i] == 'se':
        print('\'se\' was contained in Y.')
        break

    if i+1 == len(Y):
        print('\'se\' was not contained in Y.')