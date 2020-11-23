#!/usr/bin/python3


def idx_tuple(tuple, idx):
    if len(tuple) <= idx:
        return 0
    
    return tuple[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    
    tuple_c = (
        idx_tuple(tuple_a, 0) + idx_tuple(tuple_b, 0), 
        idx_tuple(tuple_a, 1) + idx_tuple(tuple_b, 1)
    )

    return tuple_c