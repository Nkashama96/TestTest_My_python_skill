'''
Dictionary Basics: Create and Access

Write a script that does the following using the specified hard-coded values:

    Creates a dictionary with the keys: name, age, and city, and the values: 'Alice', 30, and 'New York' respectively.

    Prints the dictionary.

    Prints the value for the key 'city' (which should be 'New York').

    Updates the value for the key 'age' to 31 and prints the updated dictionary.

This ensures the script can be tested for the exact expected output.

Requirements

    Create a dictionary with keys: name, age, city.

    Print the dictionary.

    Print the value for 'city'.

    Update the age and print the updated dictionary.
'''

# TODO: Create a dictionary with name, age, city
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Print the dictionary
print(person)
# Print the value for 'city'
print(person["city"])
# Update the age
person["age"] = 31
# Print the updated dictionary
print(person)
