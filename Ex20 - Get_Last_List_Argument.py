'''
Get Last List Argument

Write a function get_last_list(*args) that returns the last list argument passed to it. If no lists are passed, return an empty list.

Requirements

    The function should accept any number of arguments.

    Return the last argument that is a list, or an empty list if none are lists.
'''

def get_last_list(*args):
    last_list = []
    # TODO: Return the last list argument, or [] if none
    for arg in reversed(args):
        if isinstance(arg, list):
            last_list = arg
            return last_list
        else:
            break
    return last_list
    pass

# --- Examples ---

# Example 1: Multiple lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result1 = get_last_list(1, "hello", list1, 5.5, list2, "world")
print(f"Example 1: {result1}") # Expected: ['a', 'b', 'c']

# Example 2: Non-list arguments only
result2 = get_last_list("apple", 123, 4.5, True)
print(f"Example 2: {result2}") # Expected: []

# Example 3: Only one list
list3 = [10, 20, 30]
result3 = get_last_list("start", list3)
print(f"Example 3: {result3}") # Expected: [10, 20, 30]

# Example 4: No arguments
result4 = get_last_list()
print(f"Example 4: {result4}") # Expected: []

# Example 5: Empty lists
result5 = get_last_list([], "a", [], 1)
print(f"Example 5: {result5}") # Expected: [] 
