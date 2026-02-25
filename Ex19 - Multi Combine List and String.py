'''
Multi Combine List and String

Write a function multi_combine(lst, s) that returns a merged list containing:

    All elements from the input list

    Each unique word in the string (split by spaces, in order)

    Each unique character in the string (in order of appearance, even if already present as a word)

Requirements

    The function should take a list and a string as arguments.

    Return a list as described above.

    Words and unique characters from the string should not duplicate each other in their own group, but characters may duplicate words.
'''

def multi_combine(lst, s):
    # TODO: Return a merged list as described
    # 1. Start with all elements from the input list
    merged_list = lst[:] # Use slicing to create a copy
    
    # 2. Add each unique word in the string (split by spaces)
    words = s.split()
    seen_words = set()
    for word in words:
        if word not in seen_words:
            merged_list.append(word)
            seen_words.add(word)
            
    # 3. Add each unique character in the string (in order of appearance)
    seen_chars = set()
    for char in s:
        # Ignore spaces for character uniqueness check in the output
        if char != ' ' and char not in seen_chars:
            merged_list.append(char)
            seen_chars.add(char)
            
    return merged_list
    pass

# Example Usage:
list_input = [1, 2, 'a']
string_input = "hello world, hello python"

combined_result = multi_combine(list_input, string_input)
print(combined_result)
