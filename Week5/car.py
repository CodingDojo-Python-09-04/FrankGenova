'''
Coding Dojo - Python OOP - Assignment: Car

Created: 10/02/2017
Author: Frank J Genova

In the__init__(),
allow the user to specify the following attributes:
price, speed, fuel, mileage.
If the price is greater than 10,000, set the tax to be 15%.
Otherwise, set the tax to be 12%.
Create six different instances of the class Car.
In your __init__(), call this display_all() method to display
information about the car once the attributes have been defined.

A sample output would be like this:
Price: 2000
Speed: 35mph
Fuel: Full
Mileage: 15mpg
Tax: 0.12
'''

class Car(object):
    '''Create a class called  Car.'''
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        '''
        In the class have a method called display_all()
        that returns all the information about the car as a string.
        '''
        print('Price: ${}'.format(self.price))
        print('Speed: {} mph'.format(self.speed))
        print('Fuel: {}'.format(self.fuel))
        print('Mileage: {} mpg'.format(self.mileage))
        print('Tax: {}'.format(self.tax))
        return self

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 95)
car5 = Car(2000, 45, 'Empty', 95)
car6 = Car(20000000, 35, 'Empty', 95)
