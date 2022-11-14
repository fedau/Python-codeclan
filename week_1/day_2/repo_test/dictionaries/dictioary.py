#dictionaries are KEY -> VALUE pairs

#this is a tuple
meals = ('yoghurt', 'roll', 'steak',)
print(meals[0])

#dictionaries how to write
empyty_dictionary = {}
other_dictionary = dict()

meals = {"breakfast":"yoghurt", "lunch":"roll", "dinner":"steak"}
# print(meals)

#dictionaries can contain anything even lists, lists just can't be a key only a value
# things = {1 : "2", 'Steve': [False, 2]}
# print(things)

#printing specific value coneccted to tag
# print(meals["breakfast"])

#finding element by KEY
print("breakfast" in meals)

#adding element
meals["supper"] = "pancakes"
print(meals)

#removing element
del(meals["breakfast"])
print(meals)

#method list converts dictionary to list converst key to list
print(list(meals))

#method makes view object with a list of keys in it (why to use dunnp steve says)
print(meals.keys())

# list of the values also returns it as a view object
print(meals.values())




#nesting multiple keys in a dictionary connected to another key

countries = {
    "uk": { "capital": "London", "population": 1000},
    "germany": {"capital": "Berlin", "population": 5000}
}

#to open population "click on the first main key" "then the second key of what you want"
print(countries["germany"]["population"])