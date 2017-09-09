"""Coding Dojo - Python Fundamentals - Assignment: Checkerboard
Write a program that prints a 'checkerboard' pattern to the console.

Your program should require no input and produce console output that looks like so:
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
Each star or space represents a square.
On a traditional checkerboard you'll see alternating squares of red or black.
In our case we will alternate stars and spaces.
The goal is to repeat a process several times.
This should make you think of looping.
"""


def print_odd():
    """Print * staring with first space"""

    print("* "*4)

def print_even():
    """Print * starting with second spece"""

    print(" *"*4)

def print_checkerboard(rows):
    """Print a checkerboard with rows number of rows"""

    for row in range(1, rows+1):
        if row %2 != 0:
            print_odd()
        else:
            print_even()

print_checkerboard(8)
