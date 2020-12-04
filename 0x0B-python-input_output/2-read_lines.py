#!/usr/bin/python3
""" Read n lines  """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file """
    with open(filename) as file:
        for l, line in enumerate(file):
            print(line, end="")

            if n_lines == l + 1:
                break
