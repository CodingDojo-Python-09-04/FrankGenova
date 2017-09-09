"""Coding Dojo - Python Fundamentals - Assignment: Fun with Functions

Created: 09/03/2017
Author: Frank J Genova

Odd/Even:
Create a function called odd_even that counts from 1 to 2000.
As your loop executes have your program print the number of that iteration and specify whether
it's an odd or even number.

Output:
Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.

Multiply:
Create a function called 'multiply' that iterates through each value in a list
(e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. For example, let's say:
a = [2,4,10,16]
Then:
b = multiply(a, 5)
print b
Should print [10, 20, 50, 80 ].

Hacker Challenge:
Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional list.
Each internal list should contain the 1's times the number in the original list.
Here's an example:
def layered_multiples(arr):
      # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
"""

import os

def clear():
    """Clear the screen"""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def odd_even(start, stop):
    """Given a range of start through stop, iterate each value and determine if odd or even"""

    for number in range(start, stop):
        if number % 2 == 0:
            status = "This is an even number."
        else:
            status = "This is an odd number."
        print("Number is {}. {}".format(number, status))

def multiply(item):
    """Multiply each item by 5"""

    return item*5

def hacker(array):
    """Make new list with 1's array item number of times"""

    new_list = []
    new_array = []
    for each in array:
        for index in range(0, each):
            new_list.append("1")
        new_array.append(new_list)
        new_list = []
    return new_array

def continue_clear(function_message, instructions):
    """Print instructions and clear screen"""

    print("="*80)
    print(function_message)
    print(instructions)
    print("="*80)
    decide = input(">")
    if decide.upper() == "Q" or decide.upper == "QUIT":
        exit()
    else:
        clear()

def main():
    """Run the functions defined for the assignment see docstrings"""
    clear()
    start = 1
    stop = 2000
    function_message = ("Determine if a number is odd or even starting with {} and ending with {}".format(start, stop))
    instructions = "Press enter to clear and continue or 'Q' to QUIT"
    continue_clear(function_message, instructions)
    odd_even(1, 2000)
    array = [2, 4, 10, 16]
    by_num = 5
    function_message = ("Given an array: {} multiply each element by {} and return list.".format(array, by_num))
    continue_clear(function_message, instructions)
    target_array = list((map(multiply, array)))
    print("target array: {}".format(target_array))
    function_message = ("Given an array from multiply: {} output a list where each element has that number of 1's and return this as a list.".format(target_array))
    continue_clear(function_message, instructions)
    print(hacker(target_array))

if __name__ == '__main__':
    main()
