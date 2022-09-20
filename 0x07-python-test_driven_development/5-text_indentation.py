#!/usr/bin/python3
"""
A function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Functions returns strings with 2 new lines after every ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # for char in text:
    #     print(char, end="")
    #     if char == "." or char == "?" or char == ":":
    #         print("\n\n", end="")

    ind = 0
    """Eliminate leading space from text"""
    while ind < len(text) and text[ind] == " ":
        ind += 1

    """
    Printing text, removing leading and trailing spaces
    after new lines, and adding \n after every case of . ? and :
    """
    while ind < len(text):
        print(text[ind], end="")
        if text[ind] in ".?:\n":
            if text[ind] in ".?:":
                print("\n")
            ind += 1
            while ind < len(text) and text[ind] == ' ':
                ind += 1
            continue
        ind += 1
