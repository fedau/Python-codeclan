class PetShop:
    def __init__(self, name, pets, total_cash, ):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0


    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, cash):
        self.total_cash += cash


    def remove_pet(self, pet):
        self.pets.remove(pet)


    def find_pet_by_name(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                return pet

    
    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        customer.reduce_cash(pet.price)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        self.stock_count()
        self.remove_pet(pet)
        customer.add_pet(pet)
        customer.pet_count()
        





        # if pet != None and customer_can_afford_pet(customer, pet):
        # remove_pet_by_name(pet_shop, pet["name"])
        # add_pet_to_customer(customer, pet)
        # remove_customer_cash(customer, pet["price"])
        # add_or_remove_cash(pet_shop, pet["price"])
        # increase_pets_sold(pet_shop, 1)



        