"""Coding Dojo - Python Fundamentals - Assignement: Compare Lists"""


def compare_lists(list_one,list_two):
    """Compare lists to see if they are equivalent"""

    if list_one == list_two:
        print("Lists are the same")
    else:
        print("Lists are not the same")    

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare_lists(list_one, list_two)


list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compare_lists(list_one, list_two)