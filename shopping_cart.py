# Your program should have two separate classes: one to represent a product to be purchased and one to represent a shopping cart containing a collection of products.

# Each product has a name, base price, and tax rate. There should also be a method to calculate and return the product's total price based on the base price and tax rate.

# Each shopping cart has a collection of products. It should also have the following functionality:

# add an product to the cart
# remove an product from the cart
# add up the total cost of all products in the cart before tax
# add up the total cost of all products in the cart after tax
# Think about which class needs to make reference to the other one and remember to use a import statement accordingly. You don't need it in both files.
from product import Product

class Shopping_cart:

    def __init__(self):
        self.products =[]
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, product):
        self.products.remove(product)
    
    def total_before_tax(self):
        total = 0
        for product in self.products:
            total += product.base_price
        return total

    def total_after_tax(self):
        total = 0
        for product in self.products:
            total = total + (product.base_price * (1 + product.tax_rate / 100))
        return total

cart1 = Shopping_cart()
item1 = Product('ps4', 400, 13)
item2 = Product('vodka', 50, 20)
cart1.add_product(item1)
cart1.add_product(item2)
print(cart1.total_before_tax())
print(cart1.total_after_tax())
cart1.remove_product(item1)
print(cart1.total_before_tax())
print(cart1.total_after_tax())

    


