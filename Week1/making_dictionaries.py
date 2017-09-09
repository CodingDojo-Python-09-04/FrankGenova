"""Coding Dojo - Python Fundamentals - Assignment: Making Dictionaries

Created: 09/03/2017
Author: Frank J Genova

Create a function that takes in two lists and creates a single dictionary
where the first list contains keys and the second values.
Assume the lists will be of equal length.

Your first function will take in two lists containing some strings.
Here are two example lists:
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

Hacker Challenge:
If the lists are of unequal length, the longer list should be used for the keys,
the shorter for the values.

"""

def make_dict(arr1, arr2):
    """Zip together two lists and return as dictionary"""
    if len(arr1) >= len(arr2):
        return dict(zip(arr1, arr2))
    else:
        return dict(zip(arr2, arr1))

arr1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
arr2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

new_dict = make_dict(arr1, arr2)
print(new_dict)
