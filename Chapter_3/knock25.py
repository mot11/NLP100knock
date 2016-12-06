# -*- coding: utf-8 -*-

import re


def find_kisojouhou(str_1):

    p_1 = re.compile(r'.{2}(?=(基礎情報))')
    p_2 = re.compile(r'\{')
    p_3 = re.compile(r'\}')

    m_1 = p_1.search(str_1)
    brackets = 0

    for i in range(m_1.start(), len(str_1)):
        if p_2.match(str_1[i]):
            brackets += 1
        if p_3.match(str_1[i]):
            brackets -= 1
        if brackets == 0:
            break

    output = str_1[m_1.start():i+1]

    return output


def hoge(str_1):
    p = re.compile(r'\\n')
    return p.sub(r'\n', str_1)


def convert_dictionary(str_1):
    p = re.compile(r'(?<=\|)([^ =]+) = (((?!(\\n\||\\n\}\}$)).)*)?')

    output = {m.group(1): m.group(2) for m in p.finditer(str_1)}

    return output


def main():
    with open('uk.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    kisojouhou = find_kisojouhou(content[0])
    output = convert_dictionary(kisojouhou)

    print(output)

    print(output['略名'])

if __name__ == '__main__':
    main()
