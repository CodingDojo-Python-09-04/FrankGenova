"""Coding Dojo - Python Fundamentals - Assignment: Dictionary in, tuples out

Created: 09/03/2017
Author: Frank J Genova

Write a function that takes in a dictionary and returns a list of tuples
where the first tuple item is the key and the second is the value.
Here's an example:

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
"""

my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

new_list = []
for each in my_dict.items():
    new_list.append(each)

print(new_list)
