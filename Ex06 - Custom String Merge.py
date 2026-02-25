'''
Custom String Merge

A social media platform wants to generate unique usernames by merging two existing usernames. The rule is to remove the first character from the first username and the last character from the second username, then concatenate the results to form a new username.

Problem

Write a Python program that, given two usernames, creates a new username by removing the first character from the first username and the last character from the second username, then concatenating them.

    Input: Two variables: username1 and username2 (both strings).

    Output: Print the new username.

Example

If username1 = 'Alice' and username2 = 'Bob', the output should be:

    liceBo

    Use string slicing and concatenation.

    Your code should work for any non-empty strings.
'''

# Given two usernames, create a new username by removing the first character from the first username and the last character from the second username, then concatenate them.

username1 = 'Alice'
username2 = 'Bob'

# TODO: Print the new username 
print(f"{username1[1:]}{username2[:-1]}")
