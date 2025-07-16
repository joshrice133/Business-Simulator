import random
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
    def sell(self, customer, product):
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
    def changePrice(self, product):
        product.price = product.price + #user input
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
