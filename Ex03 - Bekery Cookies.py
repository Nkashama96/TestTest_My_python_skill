'''
Bakery needs your help with cookies count

A local bakery packs cookies into boxes, each box holding exactly 6 cookies. At the end of the day, the bakery wants to know how many cookies will be left unpacked after filling as many boxes as possible. This helps them plan for the next day's baking.

Write a Python program that, given the total number of cookies baked in a day, calculates how many cookies will be left unpacked after filling all possible boxes of 6.

Input: An integer variable total_cookies representing the total cookies baked.

Given: Today's count from the local bakery: total_cookies = 50.

Output: Print the number of unpacked cookies after boxing.


Example: If the count from the local bakery is total_cookies = 77,

Then the output should be: 5

Because 77 cookies fill 12 boxes (12*6=72), and 5 are left unpacked.
'''

import math
# Given the total number of cookies baked in a day
# print how many will be left unpacked after boxing them in boxes of 6.

total_cookies = 50  # You can change this value to test other cases
unpacked = total_cookies%6

# TODO: Print the number of unpacked cookies after boxing 

print(unpacked) 
