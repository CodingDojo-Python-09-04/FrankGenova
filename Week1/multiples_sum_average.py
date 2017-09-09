"""Coding Dojo: Multiples, Sum, Average

Created: 2017.08.31
Updated: 2017.09.01
Author: psychofarm@me.com
"""

import os

def clear():
    """Detect operating system and clear screen"""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def multiples(start, stop, step, option):
    """Print numbers from start to stop divisible by step allowing for 'not' divisible option

    >>> multiples(1, 6, 2, "not")
    1, 3, 5, 
    True

    """
    for item in range(start, stop):
        if option == "not":
            # print(item, step)
            if item % step != 0:
                if item != stop-1:
                    print(item, end=", ")
                else:
                    print(item)
                    print("_"*40)
        else:
            if item % step == 0:
                if item != stop-1:
                    print(item, end=", ")
                else:
                    print(item)
                    print("_"*40)
    print()
    return True


def list_sum_avg(arr):
    """Print the elements, sum and average of the list

    >>> arr = [1, 2, 3]
    >>> list_sum_avg(arr)
    The sum of the values: [1, 2, 3] is 6
    The average is 2.0

    """

    total = 0
    for item in arr:
        total = total + item
    average = total / len(arr)
    print("The sum of the values: {} is {}".format(arr, total))
    print("The average is {}".format(average))

def input_params():
    """Input start, stop, step and option"""

    clear()
    start_needed = True
    stop_needed = True
    step_needed = True
    option_needed = True
    while start_needed:
        print('Enter the starting number: ("Q" to quit) ')
        start = input('>')
        start_needed = check_param_is_int(start)
    while stop_needed:
        print('Enter the ending number: ("Q" to quit) ')
        stop = input('>')
        stop_needed = check_param_is_int(stop)
    while step_needed:
        print('Enter the divisible by number: ("Q" to quit) ')
        step = input('>')
        step_needed = check_param_is_int(step)
    while option_needed:
        print('Enter "NOT" for not divisible by option or enter to continue: ("Q" to quit) ')
        option = input('>')
        option.upper()
        option_needed = check_param_is_not(option)
    params = [int(start), int(stop), int(step), option]
    clear()
    return params

def check_param_is_int(param):
    """Check if param is as int"""

    if param.upper() == "Q":
        exit()
    try:
        int(param)
    except ValueError:
        print("ValueError thrown - enter a number")
        return True
    else:
        return False

def check_param_is_not(param):
    """Check if param is 'NOT' for not divisiable option"""

    if param.upper() == "Q":
        exit()
    elif param.upper() == "NOT":
        return False
    elif len(param) == 0:
        return False
    else:
        print("not an option")
        return True

def main():
    """Run assignment to demonstrate Muliples, Sum, Average
    Assignment: Multiples, Sum, Average
    This assignment has several parts. All of your code should be in one file
    that is well commented to indicate what each block of code is doing and which
    problem you are solving. Don't forget to test your code as you go!

    Multiples
    Part I - Write code that prints all the odd numbers from 1 to 1000.
    Use the for loop and don't use a list to do this exercise.

    Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

    Sum List
    Create a program that prints the sum of all the values in
    the list: a = [1, 2, 5, 10, 255, 3]

    Average List
    Create a program that prints the average of the values in
    the list: a = [1, 2, 5, 10, 255, 3]
    """

    params = input_params() #get start, stop, step, option
    start = params[0]
    stop = params[1]
    step = params[2]
    option = params[3]
    print("Print numbers {} divisible by {} from {} to {}:".format(option, step, start, stop))
    multiples(start, stop, step, option)
    # multiples(1, 1000, 2, "not") # Multiples Part I - odd numbers 1 to 1000
    # multiples(5, 1000000, 5, "") # Multiples Part II - divisible by 5 from 5 to 1,000,000
    list_sum_avg([1, 2, 5, 10, 255, 3]) # Sum List and Average List

if __name__ == '__main__':
    main()
