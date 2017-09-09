"""Coding Dojo - Python Fundamentals - Optional Assignment: NumPy

Created: 09/03/2017
Author: Frank J Genova

"""

import os
import numpy as np

matrix = np.eye(4, dtype=int)

def clear():
    """Clear the screen"""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def repeat(character, number):
    """Print character repeatedly number of times"""

    print(character*number)

def output(menu_choice, new_matrix):
    """Print output of numpy method used"""

    clear()
    make_line()
    print("Example of {}".format(menu_choice))
    print(new_matrix)

def make_line():
    """Print a line of 80 character length"""

    repeat("_", 80)

def menu():
    """Set up menu and accept input"""

    menu_dict = {"1":"eye"}
    clear()
    make_line()
    print("\nTo try out a numpy method, select the number ('Q' to quit)")
    print("\n[+] 1 - eye")
    menu_num_choice = input("\n>")
    if menu_num_choice.upper() == 'Q':
        exit()
    menu_choice = menu_dict[menu_num_choice]
    clear()
    print(menu_choice," > ")
    make_line()
    if menu_num_choice == '1':
        print("\nEnter number of rows in the output: ('Q' to quit)")
        rows = int(input("\n>"))
        new_matrix = np.eye(rows, dtype=int)
        output(menu_choice, new_matrix)

def main():
    """Pick a numpy function using menu, enter arguments and print output"""
    
    menu()

if __name__ == '__main__':
    main()
        


