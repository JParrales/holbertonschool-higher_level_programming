#!/usr/bin/python3


def roman_to_int(roman_string):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0

    if type(roman_string) != str or roman_string is None:
        return res

    previous = None
    for i in roman_string:
        n = romanos[i]

        if previous is None:
            res = n
            previous = n
            continue
        elif previous < n:
            res = res + n - previous * 2
        else:
            res += n

        previous = n

    return res
