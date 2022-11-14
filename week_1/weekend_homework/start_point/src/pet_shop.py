# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_store):
    return pet_store["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# this one can be simplified
def add_or_remove_cash(pet_shop, num):
    pet_shop["admin"]["total_cash"] += num

    # return cash ["admin"]["total_cash"]

def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]

def increase_pets_sold(pets_stock, num_sold):
    pets_stock ["admin"]["pets_sold"] += num_sold

def get_stock_count(pet_shop):
    # stock = 0
    # for pet in pet_shop ["pets"]:
    #    stock += 1
    # return stock
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_kind):
    total_breeds = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_kind:
            total_breeds.append(breed_kind)
            
    return total_breeds

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    # return None


def remove_pet_by_name(pet_shop, name):
     for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)



def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, amount):
    money_value = amount
    cash_price = customer["cash"]
    new_money_value = cash_price - money_value 
    customer["cash"] = new_money_value
#    return customer["cash"] += amount


def get_customer_pet_count(customers):
    return len(customers["pets"])



def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



def customer_can_afford_pet(customer, new_pet):
   if customer["cash"] >= new_pet["price"]:
    return True
   else:
    return False 



# def sell_pet_to_customer(pet_shop, pet, customer):
    if pet:
        pet_to_sell = find_pet_by_name(pet_shop, pet["name"])

        if pet_to_sell == None:
            return

        if not customer_can_afford_pet(customer, pet):
            return

        pet_shop["pets"].remove(pet)
        add_pet_to_customer(customer, pet)
        pet_shop["admin"]["pets_sold"] = pet_shop["admin"]["pets_sold"] + 1

        pet_shop_cash = get_total_cash(pet_shop)
        pet_shop["admin"]["total_cash"] = pet_shop_cash + pet["price"]
        remove_customer_cash(customer, pet["price"])



def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)