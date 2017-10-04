'''
Coding Dojo - Python OOP - Assignment: Animal

Created: 10/04/2017
Author: Frank J

Create an Animal class.
Extend the Animal class to two child classes, Dog and Dragon.
'''

class Animal(object):
    '''Animal class attributes and methods'''
    def __init__(self, name, health):
        '''create new Animal object'''
        self.name = name
        self.health = health
    def walk(self):
        '''decreaese health by 1'''
        print('walking')
        self.health -= 1
        return self
    def run(self):
        '''decrease health by 5'''
        print('running')
        self.health -= 5
        return self
    def display_health(self):
        '''print animal's health'''
        print ('health: {}'.format(self.health))

class Dog(Animal):
    '''Dog class extends Animal and adds pet method'''
    def __init__(self, name, health=150):
        '''create a new Dog object'''
        super(Dog, self).__init__(name, health)
    def pet(self):
        '''increse health by 5'''
        print('petting')
        self.health += 5
        return self

class Dragon(Animal):
    '''Dragon class extends Animal and adds fly method'''
    def __init__(self, name, health=170):
        '''create a new Dragon object'''
        super(Dragon, self).__init__(name, health)
    def fly(self):
        '''decrease health by 10'''
        print('flying')
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print('I am a dragon')

some_dog = Animal('Fido', 100)
print(some_dog.name, some_dog.health)
some_dog.walk().walk().walk().display_health()
fido = Dog('Fido')
fido.walk().walk().walk().run().run().pet().display_health()
kara = Dragon('Kara')
kara.fly().display_health()
# fido.fly()
# some_dog.pet()
# some_dog.fly()
some_dog.display_health()
