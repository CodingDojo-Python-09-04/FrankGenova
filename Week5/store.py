'''
Coding Dojo - Python OOP - Assignment: Store

Created: 10/03/2017
Author: Frank J Genova

'''

class Store(object):
    '''
    Build a store to contain our products by making a store class and
    putting our products into an array.
    '''

    def __init__(self, array, location, owner):
        '''
        products: an array of products objects
        location: store address
        owner: store owner's name
        '''

        self.array = array
        self.location = location
        self.owner = owner
    
    def add_product(self, product):
        '''add a product to the store's product list'''

        self.array.append(product)
        return

    def remove_product(self, product):
        '''remove a product according to the product name'''
        
        self.array.pop(self.array.index(product))

    def inventory(self):
        ''' print relevant information about each product in the store'''

        print('='*50)
        for each in self.array:
            print(each.display_info())
        print('='*50)

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

    def display_info(self):
        '''display product info'''

        print('_'*50)
        print('Price: ${}'.format(self.price))
        print('Item: {}'.format(self.item_name))
        print('Weight: {} kg'.format(self.weight))
        print('Brand: {}'.format(self.brand))
        print('Cost: ${}'.format(self.cost))
        print('Status: {}'.format(self.status))
        print('_'*50)

def main():
    '''run main program'''
    inventory1 = []
    store1 = Store(inventory1, 'Jersey', 'Frank')
    product1 = Product(150000, 'onyx', 10, 'Dior', 5000000, 'for sale')
    product2 = Product(9900, 'jade', 15, 'Ralph', 505600000, 'for sale')
    product3 = Product(69, 'emerald', 15, 'Chrissy', 5069, 'for sale')
    store1.add_product(product1)
    store1.add_product(product2)
    store1.add_product(product3)
    store1.inventory()
    store1.remove_product(product2)
    store1.inventory()
        
if __name__ == '__main__':
    main()