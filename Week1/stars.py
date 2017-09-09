"""Coding Dojo - Python Fundamentals - Assignment: Stars

Created: 09/03/2017
Author: Frank J Genova

Write the following functions.

Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x) should print the following when invoked:
****
******
*
***
*****
*******
*************************

Part II
Modify the function above. Allow a list containing integers and strings
to be passed to the draw_stars() function.
When a string is passed, instead of displaying *,
display the first letter of the string according to the example below.
You may use the .lower() string method for this part.

For example:
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x) should print the following in the terminal:
****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj
"""

def draw_stars(list_of_numbers):
    """Print lists of stars based on number provided"""

    for each in list_of_numbers:
        print("*"*each)

def draw_stars_or_letters(list_of_items):
    """Print lists of stars based on number provided or repeats first letter"""

    new_list = []
    for each in list_of_items:
        # print(each)
        if isinstance(each, int):
            for i in range(0,each):
                print("*",end='')            
        else:
            first_letter = each[0]
            for i in range(0, len(each)):
                new_list.append(first_letter.lower())
        string = "".join(new_list)        
        print(string)  
        new_list = []      

print("="*80)            
x = [4, 6, 1, 3, 5, 7, 25]
print(x)
draw_stars(x)  
print("="*80)
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print(x)
draw_stars_or_letters(x)      
print("="*80)
