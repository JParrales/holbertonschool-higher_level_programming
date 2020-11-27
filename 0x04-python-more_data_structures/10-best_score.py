#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary:
        a = list(sorted(a_dictionary.values()))[-1]
        return a
    else:
        return None
