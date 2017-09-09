"""Treehouse - Python Testing - unittest

Most of the power of testing in Python comes from the `unittest` framework
and it's `TestCase` class.
Let's look at starting a `TestCase` and writing a couple of simple tests

Created: 2017.09.02
Author: Frank J Genova
"""


import unittest
import multiples_sum_average

class MultiplesSumAverageTests(unittest.TestCase):
    """Test drive the unittest module"""

    def test_five_plus_five(self):
        """Test 5 + 5 using assert"""
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        """Test 1 + 1 using assert not equal"""
        assert 1 + 1 != 3

    def test_equal(self):
        """Test multiples with 1,6,2"""
        reply = multiples_sum_average.multiples(1, 6, 2, "divisible")
        assert reply == 5

if __name__ == '__main__':
    unittest.main()
