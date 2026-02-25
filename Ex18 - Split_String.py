'''
Split String into Unique Characters

Write a function split_chars(s) that returns a list containing each unique character from the input string, in the order they first appear.

Requirements

    The function should take a string as an argument.

    Return a list of unique characters, preserving their first appearance order.
'''

def split_chars(s):
    # TODO: Return a list of unique characters from the string, in order
    seen_chars = set()
    unique_chars_list = []
    for char in s:
        if char not in seen_chars:
            seen_chars.add(char)
            unique_chars_list.append(char)
    return unique_chars_list
    pass

pString = "Hello world!"
lString = split_chars(pString)
print(lString)
