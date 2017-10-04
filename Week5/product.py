'''
Coding Dojo - Python OOP - Assignment: Product

Created: 10/02/2017
Author: Frank J Genova

The owner of a store wants a program to track products.
Create a product class to fill the following requirements.

Product Class:
Attributes:
[+] Price
[+] Item Name
[+] Weight
[+] Brand
[+] Cost
[+] Status: default "for sale"

Methods:
[+] Sell: changes status to "sold"
[+] Add tax: takes tax as a decimal amount as a parameter and returns the price of the
item including sales tax
[+] Return: takes reason for return as a parameter and changes status accordingly.
If the item is being returned because it is defective change status to defective
and change price to 0. 
If it is being returned in the box, like new mark it as for sale.
If the box has been opened set status to used and
apply a 20% discount.
[+] Display Info: show all product details.
Every method that doesn't have to return something should return self
so methods can be chained.
'''

class Product(object):
    '''Create Product to track in store'''

    def __init__(self, price, item_name, weight, brand, cost, status='for sale'):
        '''Create a new product'''

        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        '''Sell a product'''

        self.status = 'sold'
        return self

    def add_tax(self, tax_rate):
        '''Calcuate and add tax'''

        total = (self.price * tax_rate) + self.price
        return total

    def return_product(self, return_reason):
        '''return a product and update status'''
        
        if return_reason == 'defective':
            self.price = 0
            self.status = 'defective'
        elif return_reason == 'like new':
            self.status = 'for sale'
        elif return_reason == 'open':
            self.status = 'used'
            self.price = (self.price *.20) + self.price
        return self

    def display_inf(self):
        '''display product info'''

        print('Price: ${}'.format(self.price))
        print('Item: {}'.format(self.item_name))
        print('Weight: {} kg'.format(self.weight))
        print('Brand: {}'.format(self.brand))
        print('Cost: ${}'.format(self.cost))
        print('Status: {}'.format(self.status))
        return self

def main():
    '''run main program'''

    product1 = Product(150000, 'onyx', 10, 'Dior', 5000000, 'for sale')
    product2 = Product(9900, 'jade', 15, 'Ralph', 505600000, 'for sale')
    product1.return_product('open').display_inf()
    product2.return_product('defective').display_inf()
        
if __name__ == '__main__':
    main()