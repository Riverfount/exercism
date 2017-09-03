from itertools import groupby


def decode(string):
    number = ''
    str_decoded = ''
    for char in string:
        if char.isdigit():
            number += char
        else:
            if number:
                str_decoded += char * int(number)
                number = ''
            else:
                str_decoded += char

    return str_decoded


def encode(string):
    str_encoded = ''
    my_list = [list(g) for k, g in groupby(string)]
    for group in my_list:
        g = ''.join(group)
        number = str(g.count(group[0])) if (g.count(group[0]) > 1) else ''
        str_encoded += number + group[0]
    return str_encoded

