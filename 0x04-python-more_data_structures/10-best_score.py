#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary:
        return list(sorted(a_dictionary.values()))[-1]
    else:
        return None
