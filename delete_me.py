"""Coding Dojo - Python OOP - Scratch Pad

Created: 09/05/2017
Author: Frank J Genova

"""


class User(object):
    """Class definition of User"""

    def __init__(self, name, email):
        """Set some instance variables when a new object is created"""

        self.name = name
        self.email = email
        self.logged = False

    def login(self):
        """Help user log in"""

        self.logged = True
        print(self.name + "is logged in.")
        return self


def main():
    """Create an instance of the class"""
    new_user = User("Frank", "psychofarm@me.com")
    print(new_user.email)


if __name__ == '__main__':
    main()
