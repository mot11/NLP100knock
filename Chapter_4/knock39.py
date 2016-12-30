# -*- coding: utf-8 -*-

import re
import matplotlib.pyplot as plt


def parse_word_list_bak(input_list):
    """単語とその頻度をまとめて格納したリストを受け取り、それを単語の出現頻度とその頻度をとる単語の種類数を格納したリストのリストとして返す。

    :type input_list: collections.iterable
    :param input_list:
        単語とその頻度をまとめて格納したリスト。（knock36.pyで作成されたファイルと同じフォーマット）

    :return:
        output: 単語の出現頻度とその頻度をとる単語の種類数を格納したリストのリスト。
        [[出現頻度, 種類数],[...],...]
    """

    output = []

    p = re.compile('([^\t]*)\t([0-9]*)\n')
    frequency = 0

    for line in input_list:
        m = p.match(line)
        if m:
            if int(m.group(2)) == frequency:
                output[len(output) - 1][1] += 1
            else:
                output.append([int(m.group(2)), 1])
            frequency = int(m.group(2))

    output.reverse()
    return output


def parse_word_list(input_list):
    """単語とその頻度をまとめて格納したリストを受け取り、それを単語の出現頻度を格納したリストのリストとして返す。

    :type input_list: collections.iterable
    :param input_list:
        単語とその頻度をまとめて格納したリスト。（knock36.pyで作成されたファイルと同じフォーマット）

    :return:
        output: 単語の出現頻度を格納したリスト。
    """

    output = []
    frequency = 0
    bin_no = 0

    p = re.compile('([^\t]*)\t([0-9]*)\n')

    for line in input_list:
        m = p.match(line)
        if m:
            output.append(int(m.group(2)))
            if int(m.group(2)) != frequency:
                bin_no += 1
            frequency = int(m.group(2))

    return output, bin_no


def freq_zipf(input_list):
    """単語の出現頻度順とその出現頻度をリスト化

    :param input_list:
        単語の出現頻度を格納したリスト。
    :return:
        output: 単語の出現頻度順とその出現頻度を格納したリスト。
    """

    output = []

    for i, item in enumerate(input_list):
        if len(output) > 0:
            if str(output[len(output) - 1][1]) != str(item):
                output.append([i + 1, item])
        else:
            output.append([i + 1, item])

    return output


def make_graph(input_list):
    """単語の出現頻度順とその出現頻度を格納したリストについて、グラフで表示する。

    :param input_list: 単語の出現頻度順とその出現頻度を格納したリスト
    :return:
    """
    x = []
    y = []

    for line in input_list:
        x.append(line[0])
        y.append(line[1])

    plt.plot(x, y)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()


def main():
    # neko_word_list.txtが存在する前提

    with open('neko_word_list.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 単語とその頻度の読み込み
    freq_list, bin_no = parse_word_list(content)

    #単語の出現頻度順とその出現頻度をリスト化
    output = freq_zipf(freq_list)

    # 上位１０頻度までをグラフ化
    make_graph(output)

    # 上位１０頻度を出力
    print(output[100:200])


if __name__ == '__main__':
    main()
