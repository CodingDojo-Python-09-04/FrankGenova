"""Coding Dojo - Python Fundamentals - Assignment: Scores and Grades

Created: 09/03/2017
Author: Frank J Genova

Write a function that generates ten scores between 60 and 100.
Each time a score is generated, your function should display what the grade
is for a particular score.
Here is the grade table:
Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A

Output:
Scores and Grades
Score: 87; Your grade is B
Score: 67; Your grade is D
Score: 95; Your grade is A
Score: 100; Your grade is A
Score: 75; Your grade is C
Score: 90; Your grade is A
Score: 89; Your grade is B
Score: 72; Your grade is C
Score: 60; Your grade is D
Score: 98; Your grade is A
End of the program. Bye!

Hint: Use the python random module to generate a random number

import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
random_num = random.randint()
"""

import random
random_scores = []

def get_random_scores(number_of_scores):
    for i in range(1, number_of_scores):
        random_score = random.randint(60, 100)
        random_scores.append(random_score)
    return random_scores

def print_grades(random_scores):
    for each in random_scores:
        if each >= 90:
            print("Score: {}, Your grade is A".format(each,))
        elif each >= 80:
            print("Score: {}, Your grade is B".format(each,))
        elif each >= 70:
            print("Score: {}, Your grade is C".format(each,))
        elif each >= 60:
            print("Score: {}, Your grade is D".format(each,))

random_scores = get_random_scores(10)
print_grades(random_scores)

