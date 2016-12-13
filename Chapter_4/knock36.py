# -*- coding: utf-8 -*-

import re


def make_morphemes_list(mecab_input):

    """文章の一行ごとに各形態素についての情報を格納した辞書のリストを作り、文章全体について、それをリストとして返す。

    :param mecab_input:
        MeCabによって文章が形態素解析されたリスト。

    :return:
        all_morphemes: 文章全体について、一行ずつ各形態素についての情報を格納した辞書のリストを作り、それ全体をリストとしたもの。
        [[{表層形, 基本形, 品詞, 品詞細分類1},{...},...],[...],...]
    """

    all_morphemes = []
    line_morphemes = []

    p = re.compile('([^\t]*)\t([^,]*),([^,]*),[^,]*,[^,]*,[^,]*,[^,]*,([^,]*),[^,]*,[^\n]*\n')

    for line in mecab_input:
        m = p.match(line)
        if m:
            morpheme = {'表層形': m.group(1), '基本形': m.group(4), '品詞': m.group(2), '品詞細分類1': m.group(3)}
            if morpheme['品詞細分類1'] == '句点' or morpheme['品詞細分類1'] == '空白':
                all_morphemes.append(line_morphemes.copy())
                del line_morphemes[:]
                morpheme.clear()
            elif morpheme['品詞'] != '記号':
                line_morphemes.append(morpheme.copy())
                morpheme.clear()

    return all_morphemes


def make_word_list(morphemes_list):

    """すべての単語とその出現頻度を抽出したリストを作る。

    :param morphemes_list:
        文章一行ごとの各形態素についての情報を格納した辞書のリスト。

    :return:
        word_list: 全ての単語とその出現頻度を抽出したリスト。
    """

    word_list = []

    for line in morphemes_list:
        for morpheme in line:
            if morpheme['品詞'] != '記号':

                word_flag = False

                for word in word_list:
                    if morpheme['基本形'] == word[0]:
                        word[1] += 1
                        word_flag = True
                        break

                if not word_flag:
                    word_list.append([morpheme['表層形'], 1])

    return word_list


def merge_list(list_in, element, a, b, c):
    """ merges arrays in list_in at list_value[a..b] and list_value[b+1...c].

    :param list_in:
    :param element:
    :param a:
    :param b:
    :param c:
    :return: output: returns merged array.
    """

    length1 = b - a + 1
    length2 = c - b

    # dummy list
    hoge_a = []
    hoge_b = []

    for i in range(0, length1):
        hoge_a.append(list_in[a + i])

    for i in range(0, length2):
        hoge_b.append(list_in[b + 1 + i])

    # Index of first, second, and merged arrays

    i = 0
    j = 0
    k = a

    while i < length1 and j < length2:
        if float(hoge_a[i][element]) > float(hoge_b[j][element]):
            list_in[k] = hoge_a[i]
            i += 1
        else:
            list_in[k] = hoge_b[j]
            j += 1
        k += 1

    while i < length1:
        list_in[k] = hoge_a[i]
        i += 1
        k += 1

    while j < length2:
        list_in[k] = hoge_b[j]
        j += 1
        k += 1

    output = list_in[:]
    return output


def merge_sort(list_in, element, l, r):

    """ Does a merge sort of lists in list_in.

    :param list_in: List of lists. Each list contains elements that are moved together when sorting.
    :param element: Index of the element in each list that the sorting is based on.
    :param l: first element
    :param r: last element
    :return: output: returns sorted list
    """

    output = list_in[:]

    if l < r:
        m = int((l+r)/2)
        output = merge_sort(output, element, l, m)
        output = merge_sort(output, element, m + 1, r)
        output = merge_list(output, element, l, m, r)

    return output


def main():

    with open('neko.txt.mecab', 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 形態素解析結果の読み込み
    neko_morphemes = make_morphemes_list(content)

    # 単語とその出現頻度を抽出したリストの作成
    word_list = make_word_list(neko_morphemes)

    # word_listのソート
    output = merge_sort(word_list, 1, 0, len(word_list)-1)

    # word_listの出力
    output_string = '\n'.join(['\t'.join([str(x) for x in item]) for item in output])

    with open('neko_word_list.txt', 'w', encoding='utf-8') as f:
        f.write(output_string)
        f.close()

    # リストの出力
    # print(output[:40])


if __name__ == '__main__':
    main()
