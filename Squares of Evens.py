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
