'''Coding Dojo - OOP - Assigntment: Bike

Created: 10/01/2017
Author: Frank J. Genova

Create a new class called Bike with the following properties/attributes:
price, max_speed, miles
Create 3 instances of the Bike class.

What would you do to prevent the instance from having negative miles?
change self.miles -=5 to if self.miles > 6: self.miles -=5

Which methods can return self in order to allow chaining methods?
displayInfo(), ride(), reverse()
'''

class Bike(object):
    '''bike class with init and functions to ride bike'''

    def __init__(self, price, max_speed, miles=0):
        '''
        Use the __init__() function to specify the price and max_speed of each instance 
        (e.g. bike1 = Bike(200, "25mph"); 
        In the __init__() also write the code so that the initial miles is set to be 0 
        whenever a new instance is created.
        '''

        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        '''
        displayInfo() - have this method display the bike's 
        price, maximum speed, and the total miles.
        '''

        print('price: {}'.format(self.price))
        print('maximum speed: {}'.format(self.max_speed))
        print('total miles: {}'.format(self.miles))
        return self

    def ride(self):
        '''
        ride() - have it display "Riding" on the screen and
        increase the total miles ridden by 10
        '''

        self.miles += 10
        print('riding')
        return self

    def reverse(self):
        '''
        reverse() - have it display "Reversing" on the screen and 
        decrease the total miles ridden by 5...
        '''

        self.miles -=5
        print('reversing')
        return self   

bike1 = Bike('$100', '1 mph')
bike2 = Bike('$200', '2 mph')
bike3 = Bike('$300', '3 mph')
# # Have the 1st instance ride 3 times, reverse 1 and have it displayInfo(). 
bike1.ride().ride().ride().reverse().displayInfo()

# # Have the 2nd instance ride 2, reverse 2 and have it displayInfo(). 
bike2.ride().ride().reverse().reverse().displayInfo()

# # Have the 3rc instance reverse 3 times and displayInfo().
bike3.reverse().reverse().reverse().displayInfo()
