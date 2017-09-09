"""Coding Dojo - Python Fundamentals - Assignement: Coin Tosses

Created: 09/03/2017
Author: Frank J Genova

Assignment: Coin Tosses
Write a function that simulates tossing a coin 5,000 times.
Your function should print how many times the head/tail appears.

Sample output should be like the following:

Starting the program...
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
Hint: Use the python built-in round function to convert that floating point number into an integer

"""

import random


def toss_coin():
    """Simulate coint toss and return results"""

    coin = round(random.random())
    if coin == 0:
        return ("It's a head!", 1, 0)
    else:
        return ("It's a tail!", 0, 1)

def repeat_toss(number):
    """Repeat toss_coin and print results and running tally"""
    heads = 0
    tails = 0
    for attempt in range(1, number):
        coin_toss = toss_coin()
        toss = coin_toss[0]
        heads += coin_toss[1]
        tails += coin_toss[2]
        print("Attempt #{}: Throwing a coin... {} ... Got {} head(s) so far and {} tails(s) so far".format(attempt, toss, heads, tails))
    print("Ending the program, thank you!")

repeat_toss(5000)
