# -*- coding: utf-8 -*-

import re
import numpy as np
import matplotlib.pyplot as plt


def read_word_list(input_list):
    """単語とその頻度をまとめて格納したリストを受け取り、それを単語とその頻度を格納したリストのリストとして返す。

    :param input_list:
        単語とその頻度をまとめて格納したリスト。（knock36.pyで作成されたファイルと同じフォーマット）

    :return:
        output: 単語とその頻度を格納したリストのリスト。
        [[表層形, 頻度],[...],...]
    """

    output = []

    p = re.compile('([^\t]*)\t([0-9]*)\n')

    for line in input_list:
        m = p.match(line)
        if m:
            output.append([m.group(1), m.group(2)])
    return output


def make_graph(input_word_list):
    """単語とその頻度を格納したリストのリストについて、上から１０語をグラフで表示する。

    :param input_word_list: 単語とその頻度を格納したリストのリスト
    :return:
    """

    frequency = []
    words = []

    for line in input_word_list:
        frequency.append(int(line[1]))
        words.append(line[0])

    x_values = np.arange(1, len(words) + 1, 1)

    fig, ax = plt.subplots()

    plt.bar(x_values, frequency, align='center', width = 1)
    plt.suptitle('上位１０語の出現頻度')

    plt.yticks()
    plt.xticks(x_values, words)
    ax.set_ylabel('頻度')
    ax.set_xlabel('単語')

    plt.show()


def main():
    # neko_word_list.txtが存在する前提

    with open('neko_word_list.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 単語とその頻度の読み込み
    output = read_word_list(content)

    # 上位１０語までをグラフ化
    make_graph(output[:10])

    # 上位１０語を出力
    # print(output[:10])


if __name__ == '__main__':
    main()
