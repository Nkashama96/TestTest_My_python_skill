'''
Combine Lists Without Duplicates

Problem Statement

Write a function combine_lists(list1, list2) that returns a new list containing all elements from both input lists, but with no duplicate values.

Requirements

    The function should take two lists as arguments.

    Return a new list with all elements from both lists, but no duplicates.

    The order of elements should be preserved as much as possible.
'''

def combine_lists(list1, list2):
    # TODO: Return a new list with all elements from both lists, no duplicates
      combined_list = []
      # Iterate through list1 and add elements if not already present
      for item in list1:
        if item not in combined_list:
          combined_list.append(item)
      
      # Iterate through list2 and add elements if not already present
      for item in list2:
        if item not in combined_list:
          combined_list.append(item)
          
      return combined_list
      pass

List1 = ['a','b','c','d','e','g']
List2 = ['a','e','i','o','u']
List3 = combine_lists(List1,List2)
print(List3)
