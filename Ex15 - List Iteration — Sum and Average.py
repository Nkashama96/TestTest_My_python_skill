'''
List Iteration — Sum and Average

Write a function that takes a list of numbers and performs the following tasks:

    Iterates through the list and prints each number on a separate line.

    Calculates the sum of all the numbers in the list and prints it in the format Sum: <sum>.

    Calculates the average of the numbers and prints it in the format Average: <average>.

The function should handle any list of numbers (integers or floats) and print the results in the specified format.

Requirements

    Print each number in the list.

    Print the sum and average.
'''
def print_sum_and_average(numbers):
    for n in numbers:
        print(n)
    total = sum(numbers)
    avg = total / len(numbers)
    print("Sum:", total)
    print("Average:", avg)
pass

my_list = [1,2,3,4]
print_sum_and_average(my_list)
