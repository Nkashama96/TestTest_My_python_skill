'''
List Basics: Add, Remove, and Access

Write a script that creates a list of five fruits, prints the list, adds a new fruit to the end, removes the first fruit, and prints the updated list.

Requirements

Create a list with these five fruit names (in order): ['apple', 'banana', 'cherry', 'date', 'elderberry'].

Print the list.

Add the fruit 'fig' to the end.

Remove the first fruit.

Print the updated list.
'''

# TODO: Create a list of five fruits
Fruit = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Print the list
print(Fruit)
# Add a new fruit to the end
Fruit.append('fig')
# Remove the first fruit
# del Fruit[0]
Fruit.pop(0)
# Print the updated list
print(Fruit)
