class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunk = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def drunken(self, drink):
        self.drunk += drink.alcohol

    


