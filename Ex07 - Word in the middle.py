'''
Insert Word in the Middle

A puzzle game developer wants to create a feature where a word is inserted exactly in the middle of a given string. The string will always have an even number of characters. This feature will be used to generate new puzzle clues.

Problem

Write a Python program that, given a string of even length and a word, inserts the word exactly in the middle of the string and prints the result.

    Input: Two variables: container (a string of even length) and word (the word to insert).

    Output: Print the new string with the word inserted in the middle.

Example

If container = '<<>>' and word = 'puzzle', the output should be:

    <<puzzle>>

    Use the len() function and string slicing.

    Your code should work for any even-length string and any word.
'''

# Given a string of even length and a word, insert the word exactly in the middle of the string and print the result.

container = '<<>>'
word = 'puzzle'

# TODO: Print the new string with the word inserted in the middle 
new_word = container[0:2]+word+container[-2:]
print(new_word)
