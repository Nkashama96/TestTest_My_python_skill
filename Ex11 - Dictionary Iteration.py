'''
Dictionary Iteration: Keys and Values

Write a function that takes a dictionary and prints all keys, all values, and all key-value pairs.

Requirements

    Print all keys.

    Print all values.

    Print all key-value pairs.
'''

def print_dict_info(d):
    DKey = list(d.keys())
    DValue = list(d.values())
    DItem = list(d.items())
    print(d)
    # TODO: Print all keys, values, and key-value pairs
    print(f"Keys: {DKey}")
    print(f"Values: {DValue}")
    print(f"Items: {DItem}")
    
    
d = {"name":"Alice","age":30,"city":"New York"}
print_dict_info(d)
