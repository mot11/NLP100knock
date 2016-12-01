# -*- coding: utf-8 -*-

def time(x, y, z):

    output_string = str(x) + '時の' + str(y) + 'は' + str(z)
    return output_string


t_output = time(12, '気温', 22.4)
print t_output
