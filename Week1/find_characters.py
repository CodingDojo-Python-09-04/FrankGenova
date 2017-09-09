"""Coding Dojo - Python Fundamentals - Assignement: Find Characters
Write a program that takes a list of strings and a string containing a single character,
and prints a new list of all the strings containing that character.

Here's an example:
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']

Hint: how many loops will you need to complete this task?
"""
# pylint: disable=C0103

word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
new_list = []

def find_char(word_list, char):
    """Accept list of words and character, return list of words that contain character"""
    for word in word_list:
        if word.find(char) != -1:
            new_list.append(word)
    return new_list

print(find_char(word_list, char))
