# -*- coding: utf-8 -*-

import re


def make_morphemes_list(mecab_input):

    # 一行ごとの辞書のリストを作る。
    # [[{表層形, 基本形, 品詞, 品詞細分類1},{...},...],[...],...]

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


def make_noun_seq_list(morphemes_list):

    # すべての名詞の連接を抽出したリストを作る。
    seq_list = []

    # 名詞の連接
    seq = ''

    # 名詞の連接が存在する始点と終点のインデックスのリストを作る
    seq_index_list = [None] * 2

    # 始点と終点のインデックス

    for x in morphemes_list:

        # 今の位置が名詞の連接内であることを示すフラッグ
        seq_is_true = False

        for i, item in enumerate(x):

            # 前の形態素が名詞であった場合
            if seq_is_true:

                # 今の形態素が名詞である場合
                if item['品詞'] == '名詞':
                    seq_index_list[1] += 1
                else:
                    # 名詞の連接が終了した場合、seq_listに追加する
                    if seq_index_list[1] - seq_index_list[0] > 0:

                        seq = ''.join(y['表層形'] for ind, y in enumerate(x) if seq_index_list[1] >= ind >= seq_index_list[0])
                        seq_list.append(seq)

                    seq_is_true = False

            else:

                # 今の形態素が名詞である場合
                if item['品詞'] == '名詞':
                    seq_index_list[0] = i
                    seq_index_list[1] = i
                    seq_is_true = True

    return seq_list


def main():

    with open('neko.txt.mecab', 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 形態素解析結果の読み込み
    neko_morphemes = make_morphemes_list(content)

    # サ変接続の名詞の表層形を抽出したリストの作成
    seq_list = make_noun_seq_list(neko_morphemes)

    # リストの出力
    #print(seq_list[:40])


if __name__ == '__main__':
    main()