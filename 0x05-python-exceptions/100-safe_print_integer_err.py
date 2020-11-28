#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    out = True

    try:
        print('{:d}'.format(value))

    except (ValueError, TypeError) as error:
        out = False
        print('Excepion: {}'.format(error), fiel=stderr)

    return out
