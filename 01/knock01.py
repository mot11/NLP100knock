#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_line1 = raw_input('入力して下さい\n')
input_line1 = input_line1.decode('utf-8')

out = input_line1[0] + input_line1[2] + input_line1[4] + input_line1[6]

print '1,3,5,7文字目を取り出して連結した文字列は',

print out
