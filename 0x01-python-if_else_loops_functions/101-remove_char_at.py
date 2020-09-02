#!/usr/bin/python3


def remove_char_at(str, n):
    str2 = str

    if len(str) <= n or n < 0:
        return str2

    str2 = str2[0: n:] + str2[n + 1:]

    return str2
