'''
Embedding a Word in a Tag

A web developer is creating a tool to automatically wrap words with HTML tags for formatting. For example, the word 'bold' should be wrapped as bold. The developer wants a program that can insert any word between the opening and closing tags of a given HTML tag string.

Problem

Write a Python program that, given a tag string (e.g., '') and a word, prints the word embedded between the opening and closing tags.

    Input: Two variables: tag (a string like '') and word (the word to embed).

    Output: Print the result with the word inserted between the tags.

Example

If tag = '<i></i>' and word = 'italic', the output should be:

    <i>italic</i>

    Use string slicing to insert the word between the tags.

    Your code should work for any valid HTML tag string and word.
'''

# Given a tag string and a word, print the word embedded between the opening and closing tags.

tag = '<b></b>'
word = 'bold'

# TODO: Print the word embedded between the tags 
print(f"{tag[0:3]}{word}{tag[-4:]}")
