'''
Get Second-to-Last Item from Keyword List

Write a function get_second_last_item(key, **kwargs) that returns the second-to-last item in the list specified by key in the keyword arguments. If the key is not found or the list is too short, return None.

Requirements

    The function should accept a key and any number of keyword arguments.

    Return the second-to-last item in the list specified by the key.

    If the key is not found or the list is too short, return None.
'''

def get_second_last_item(key, **kwargs):
    # TODO: Return the second-to-last item in the specified list, or None
    if key in kwargs:
        value = kwargs[key]
        # Check if the value is a list (or similar sequence) and has at least 2 items
        if isinstance(value, list) and len(value) >= 2:
            return value[-2]
    return None

    pass

# --- Example Usage ---

# Example 1: Key found and list is long enough
data1 = {'list_a': [10, 20, 30, 40], 'other_data': 'test'}
second_last1 = get_second_last_item('list_a', **data1)
print(f"List A second-to-last item: {second_last1}") # Expected: 30

# Example 2: Key not found
data2 = {'list_b': [1, 2], 'other_data': 'test'}
second_last2 = get_second_last_item('list_a', **data2)
print(f"List A second-to-last item (key missing): {second_last2}") # Expected: None

# Example 3: List is too short (only one item)
data3 = {'list_c': [100]}
second_last3 = get_second_last_item('list_c', **data3)
print(f"List C second-to-last item (list too short): {second_last3}") # Expected: None

# Example 4: Value is not a list
data4 = {'not_a_list': "a string"}
second_last4 = get_second_last_item('not_a_list', **data4)
print(f"Not a list: {second_last4}") # Expected: None