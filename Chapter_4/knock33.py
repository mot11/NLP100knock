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


def make_noun_list(morphemes_list):

    # すべてのサ変接続の名詞の表層形を抽出したリストを作る。

    noun_list = []

    for x in morphemes_list:
        for y in x:
            if y['品詞'] == '名詞' and y['品詞細分類1'] == 'サ変接続':
                noun_list.append(y['表層形'])

    return noun_list


def main():

    with open('neko.txt.mecab', 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 形態素解析結果の読み込み
    neko_morphemes = make_morphemes_list(content)

    # サ変接続の名詞の表層形を抽出したリストの作成
    noun_list = make_noun_list(neko_morphemes)

    # リストの出力
    print(noun_list[:40])


if __name__ == '__main__':
    main()