class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, bill):
        self.till += bill

    
    def buy_drink(self, customer, drink):
        if self.check_age(customer):
            self.till += drink.price
            customer.reduce_wallet(drink.price)


    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def check_drunkenness(self, customer, drink):
        if customer.drunk <= 4:
            self.buy_drink(customer,drink)
            customer.drunken(drink)
        else: 
            return "you are to drunk"

    def buy_food(self, customer, food):
        customer.wallet -= food.price
        bill = food.price
        self.increase_till(bill)
        customer.drunk -= food.rejuvenation

 

  


        