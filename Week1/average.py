"""Treehouse - Python Testing - Challenge Task 1 of 1
Add a doctest to average() that tests the function with the list [1, 2].
Because of how we test doctests, you'll need to leave a blank line
at the end of your doctest before the closing quotes.
"""


def average(num_list):
    """Return the average for a list of numbers

    >>> average([1, 2])
    1.5

    """

    return sum(num_list) / len(num_list)
