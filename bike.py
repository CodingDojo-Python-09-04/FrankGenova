"""Coding Dojo > Python/Django Online > Python OOP > Python OOP > Bike

Created: 09/06/2017
Author: Frank J Genova

"""

import os
import random

def clear():
    """Clear the screen"""

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class Bike(object):
    """Bike class"""

    def __init__(self, price, max_speed, miles):
        """create new instance of bike with price, max_speed and miles"""

        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        """Diplay info about bike"""

        print("="*80)
        print("Bike #{} has the following:".format(bike))
        print("price: {}".format(self.price))
        print("max_speed: {}".format(self.max_speed))
        print("miles: {}".format(self.miles))
        print("="*80)        

bike1 = Bike(100, 12mph, 0)
bike2 = Bike(200, 24mph, 0)
bike3 = Bike(200, 30mph, 0)

Bike.displayInfo(bike1)
Bike.displayInfo(bike2)
Bike.displayInfo(bike3)
