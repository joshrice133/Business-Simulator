import random

# Is this supposed to be in global scope? 
# Global variables are typically a hard no
# unless there is literally no other way around them
sellquantity = 0

class Business:
    def __init__(self):
        self.gRev = 0
        self.expenses = 0
        self.income = 0
        self.bank = 0
        self.products = {}
        self.customers = []
        self.employees = []
        self.productiveCapital = 0
    # This should return something to the Customer. Idk if the product obj 
    # is the right move, but you get the idea. Also, the argument should just be
    # the product name.
    # Perhaps a purchase receipt?

    # You should get into the habit of using type and return annotations
    def sell(self, product_name: str) -> Product:
        # Try-except blocks allow you to handle errors as they show up
        # anything that might be error prone, such as checking range values,
        # should be wrapped in a try-except so your program doesn't crash 
        # if it runs into problems
        # This is just a rudimentary example, but you get the idea.
        try:
            if self.products[product_name] <= 0:
                # I don't actually know if "throw" is a python keyword (it might be java)
                # But there should be a way to invoke an exception in python
                throw OutOfStock
            else:
                self.products[product_name] -= 1
                return Product(product_name)
        except OutOfStock:
            return "OutOfStock!"


        # This is trying to do too much.
        # The inputs should be a product name and the output
        # should be some value or object that the Customer can use.
        """
        if self.products[product] == 0:
            print(product + " is not in stock!.")
            return
        if self.products[product] < 0:
            print("Error: Product cannot be less than 0.")
        for customer in self.customers:
            if customer.interest[product] >= 20 and customer.productAwareness[product] == True:
                sellquantity = random.randint(6,10)
                self.gRev += product.price * sellquantity
                self.products[product] -= sellquantity
            elif customer.interest[product] >= 20 and customer.productAwareness[product] == True:
                sellquantity = random.randint(3,5)
                self.gRev += product.price * sellquantity
                self.products[product] -= sellquantity
            elif customer.interest[product] >= 20 and customer.productAwareness[product] == True:
                sellquantity = random.randint(1,2)
                self.gRev += product.price * sellquantity
                self.products[product] -= sellquantity
            else:
                print("No customers are interested in " + product)
            """
    def changePrice(self, product, price: int):
        product.price = price

    # I would comment this so others (like myself) know what you're doing
    def market(self, product):
        rollA = 0
        rollB = 0
        customersAware = 0
        customersInterested = 0
        self.bank = self.bank - 10
        for customer in self.customers:
            rollA = random.randint(1,2)
            rollB = random.randint(1,4)
            if rollA == 1:
                customer.productAwareness[product] = customer.productAwareness[product] == True
            if rollB == 1 and customer.productAwareness[product] == True:
                customer.interest[product] = customer.interest[product] + 5
    def buyMats(self):
        
    def hire(self):
    def fire(self):
    def rnd(self):
    def expand(self):
