"""Coding Dojo - Python Fundamentals - Optional Assignment: Foo and Bar
Write a program that prints all the prime numbers and all the perfect squares for all numbers
between 100 and 100000.

For all numbers between 100 and 100000 test that number 
for whether it is prime or a perfect square.
If it is a prime number print "Foo". If it is a perfect square print "Bar".
If it is neither print "FooBar". Do not use the python math library for this exercise.
For example, if the number you are evaluating is 25,
you will have to figure out if it is a perfect square. It is, so print "Bar".

This assignment is extra challenging! Try pair programming and pulling up a white board.
"""

array = []
not_prime = []
perfect_square = []
square = 1

for num in range(100,10000):
    array.append(num)

for divisor in range(2,10000):
    for each in array:
        if each != divisor and each % divisor == 0:
            if each not in not_prime:
                not_prime.append(each)
                if each in array:
                    array.remove(each)
print("Foo - prime numbers:")
print(array)

not_prime.sort()

multiplier = 2
for multiplier in range(2,10000):
    square=multiplier*multiplier
    if square in not_prime:
        perfect_square.append(square)
        not_prime.remove(square)
    if square > 10000:
        break

print("Bar - Perfect square: {}".format(perfect_square))
print("Foo - Prime numbers: {}".format(array))    
print("FooBar - All others not prime or perfect square: {}".format(not_prime))

