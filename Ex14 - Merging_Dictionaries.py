'''
Merging Dictionaries

Write a function merge_dicts(dict1, dict2) that merges two dictionaries. If a key exists in both dictionaries, the value from dict2 should be used in the result.

Function Requirements

    The function should take two dictionaries as arguments.

    Return a new dictionary containing all keys and values from both input dictionaries.

    If a key exists in both dictionaries, the value from dict2 should be used.
  '''

def merge_dicts(dict1, dict2):
    # TODO: Merge two dictionaries, using values from dict2 for duplicate keys
    return {**dict1, **dict2}
    pass
