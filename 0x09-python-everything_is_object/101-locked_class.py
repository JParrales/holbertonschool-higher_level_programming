#!/usr/bin/python3
""" Low memory cost  """


class LockedClass:
    """ prevents the user from dynamically creating new attributes """

    __slots__ = ['first_name']
