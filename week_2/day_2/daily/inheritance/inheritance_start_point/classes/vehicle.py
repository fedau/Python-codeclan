class Vehicle:
# inheritance can be bad because now you have to add a price to all its children
# favor composition over inheritance
    # def __init__(self, price):
    #     self.price = price

    def start_engine(self):
        return "Vrrmmm"