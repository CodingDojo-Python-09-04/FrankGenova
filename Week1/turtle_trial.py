"""Coding Dojo - Python Funadamental - Optional Assignment: Python Turtle

Created: 09/13/2017
Author: Frank J Genova

Try drawing a simple picture using the Python module Turtle.

Turtle is a Python drawing module for kids.
It uses Python's built-in ability to test GUI apps as you write the code.
Even though it's for kids, you can do some complex drawing with it.
Learning new technologies, languages, modules, plugins, and libraries is
a very common practice for any programmer.
When you learn about something new, make sure to try it, even if it's silly!
Being curious is key to being a good developer!

Here is an example of what we can do using Turtle:

# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20
"""

import turtle
import random

# the distance we want the pointer to travel each time
DIST = 10
wn = turtle.Screen()
frank = turtle.Turtle()

# Determines the number of objects to be draw
for objects in range(1,10):
    for x in range(0, 10):
        sides = random.randint(4,20)
        for y in range(1, sides):
            # print("y", y)
            # turn the pointer 90 degrees to the right
            frank.right(360/sides)
            # advance according to set distance
            frank.forward(DIST)
        # add to set distance
        DIST += 5
