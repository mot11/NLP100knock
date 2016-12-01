#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

line1 = 'パトカー'

line2 = 'タクシー'

max_length = 0

if len(line1) >= len(line2):
    max_length = len(line1)
else:
    max_length = len(line2)

for i in range(max_length):
    sys.stdout.write(line1[i])
    sys.stdout.write(line2[i])
