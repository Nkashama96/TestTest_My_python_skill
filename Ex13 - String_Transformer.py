'''
String Transformer

Write a function string_transform(s) that takes a string and returns a tuple with:

    The reversed string

    The string in uppercase

    The string with all vowels removed (a, e, i, o, u, both cases)

Function Requirements

    The function should take a single string argument.

    Return a tuple: (reversed string, uppercase string, string with vowels removed)

    Vowels to remove: a, e, i, o, u (both lowercase and uppercase)
'''

def string_transform(s):
    # TODO: Return (reversed string, uppercase string, string with vowels removed)
    reversed_string = s[::-1]
    
    upper_string = s.upper()

    vowels = "aeiouAEIOU"
    # A generator expression filters out characters that are present in the vowels string
    # and the join method concatenates the remaining characters into a new string.
    NoVowels_string = "".join(char for char in s if char not in vowels)
    return reversed_string, upper_string, NoVowels_string
    pass

original_string = "Hello World"
result = string_transform(original_string)
print(result)
