

#define non-empty tuple
car = ('Ford', 'Escort', 1300, 'Red')
car2 = 'Ford', 'Escort', 1300, 'Red'
print(type(car2))

# define an empty tuple
empty_tuple = ()
also_empty = tuple()

# access value by index
model = car[1]
colour = car[-1]
print(f"model: {model} colour: {colour}")

#can't modify though!
# car[1] = 'Focus'

#length tuple elements
tuple_count = len(car)
print(tuple_count)

#count how many same element
fruits = ("ap", "ap", "ba")
print(fruits.count("ba"))

#tuple of a single element
single_tuple = ('ben')
print(type(single_tuple))