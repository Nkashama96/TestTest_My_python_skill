'''
Squares of Evens

Write a function squares_of_evens(numbers) that returns a list of the squares of all even numbers from the input list.

Function Requirements

    The function should take a list of integers as input.

    Return a list containing the squares of all even numbers from the input list.

    Use a list comprehension for the solution.
'''
def squares_of_evens(numbers):
    square_of_even = []
    # TODO: Return a list of squares of even numbers from the input list
    for number in numbers:
        if number%2 == 0: 
            square = number ** 2
            square_of_even.append(square)
        else:
            print( number)
    return square_of_even
    pass

my_list = [2,4,6]
print(squares_of_evens(my_list))
