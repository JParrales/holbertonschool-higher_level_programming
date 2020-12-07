#!/usr/bin/python3
"""
3. Print square
Function that prints a text with 2 new lines
after each of these characters: ., ? and :
Prototype: def text_indentation(text):
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")

    new_str = "".join([x if x not in ".?:" else x + "\n\n" for x in text])
    print("\n".join([x.strip() for x in new_str.split("\n")]), end="")
