'''
Dictionaries: Merging Dictionaries

Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key exists in both dictionaries, the value from dict2 should be used in the result.

Function Requirements

    The function should take two dictionaries as arguments.

    Return a new dictionary containing all keys and values from both input dictionaries.

    If a key exists in both dictionaries, the value from dict2 should be used.
'''

def merge_dicts(dict1, dict2):
    # TODO: Merge two dictionaries, using values from dict2 for duplicate keys
    """
    Merges two dictionaries.

    If a key exists in both dict1 and dict2, the value from dict2 is used.

    Args:
        dict1: The first dictionary (base).
        dict2: The second dictionary (overwrites conflicts in dict1).

    Returns:
        A new dictionary containing the merged key-value pairs.
    """
    # Unpack dict1 first, then unpack dict2.
    # When keys overlap, the later value (from dict2) overwrites the earlier one.
    return {**dict1, **dict2}

# --- Example Usage ---
dict_a = {'a': 1, 'b': 2, 'c': 3}
dict_b = {'b': 99, 'd': 4}

merged = merge_dicts(dict_a, dict_b)
print(f"Dictionary A: {dict_a}")
print(f"Dictionary B: {dict_b}")
print(f"Merged Dictionary: {merged}")

# Expected output: {'a': 1, 'b': 99, 'c': 3, 'd': 4}
