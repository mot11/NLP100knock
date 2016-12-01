#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

line1 = 'パトカー'
line1_u = line1.decode('utf-8')

line2 = 'タクシー'
line2_u = line2.decode('utf-8')

max_length = 0

if len(line1_u) >= len(line2_u):
    max_length = len(line1_u)
else:
    max_length = len(line2_u)

for i in range(max_length):
    sys.stdout.write(line1_u[i])
    sys.stdout.write(line2_u[i])

print ''
