#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r') as file:
        print(file.read(), end="")