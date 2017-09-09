"""Coding Dojo - Python Fundamentals - Assignment: Type List

Created: 2018.09.02
Author: Frank J Genova

Write a program that takes a list and prints a message for each element
in the list, based on that element's data type.

Your program input will always be a list. For each item in the list,
test its data type. If the item is a string, concatenate it onto
a new string. If it is a number, add it to a running sum.
At the end of your program print the string,
the number and an analysis of what the list contains.
If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too.
What kind of unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"

# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"

"""

# pylint: disable=C0103

def process_list(l):
    """Concatenate strings and add sums"""

    str_count = 0
    int_count = 0
    new_str = []
    new_sum = 0
    for item in l:
        if isinstance(item, str):
            # print("{} is a string".format(item))
            new_str.append(item)
            str_count += 1
        elif isinstance(item, (int, float, complex)):
            # print("{} is a number".format(item))
            new_sum += item
    if str_count > 0 and new_sum > 0:
        list_type = "mixed"
        print("String: "," ".join(new_str))
        print("Sum: {}".format(new_sum))
    elif str_count > 0:
        list_type = "string"
        print("String: {}".format(" ".join(new_str)))
    else:
        list_type = "integers"
        print("Sum: {}".format(new_sum))
    print("The list you entered is of {} type.".format(list_type))

if __name__ == '__main__':
    l = ['magical unicorns', 19, 'hello', 98.98, 'world']
    process_list(l)
    l = [2,3,1,7,4,12]
    process_list(l)
    l = ['magical','unicorns']
    process_list(l)