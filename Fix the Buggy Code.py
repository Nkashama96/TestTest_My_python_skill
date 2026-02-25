'''
You are given a function print_variables() that is supposed to demonstrate the use of Python's basic data types: int, float, bool, and str. However, there is a bug in the code where a string is incorrectly assigned to an integer variable. Your task is to fix the bug and ensure the function prints all variables in the specified format.

Requirements

Fix the incorrect assignment that assigns a string value to an integer variable.

Print all variables using the following format:

    Integer: -1000000000

    Float: 394.003

    Boolean: False

    String: %

Use the correct Python data types for each variable.
'''

# TO DO: Fix the Incorrect assignment
def print_variables():
    float_var = 394.003
    integer_var = -1000000000
    boolean_var = False
    string_var = "%"


    print("Integer:", integer_var)
    print("Float:", float_var)
    print("Boolean:", boolean_var)
    print("String:", string_var)
