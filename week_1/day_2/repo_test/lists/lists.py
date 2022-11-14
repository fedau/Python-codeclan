# create empty lists
empty_1 = []
empty_2 = list()

#create a list with items
fruits = ["apple", 'banana', 'orange',]


# reassinging value at index
fruits[1] = "mango"
# print(fruits)

# get the number of items
# print(len(fruits))

num_of_fruits = len(fruits)
# print(num_of_fruits)

#remove last element
removed_fruits = fruits.pop()
print(f'I removed {removed_fruits}')

# add a new fruit 
fruits.append("pear")

print(fruits)