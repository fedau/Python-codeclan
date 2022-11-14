#do not repeat yourself


###while loop

# counter = 0
# my_number = 5

# while(counter < my_number):
#     print(f"counter is {counter}")
#     counter += 1

##find my number
# my_number = 5
# value = int(input("what number am i thinking off?"))

# while (value != my_number):
#     value =int(input("nope try again....."))

# print("yes correct")

## another loopdiedoop
# while(True):
#     line = input("type something: ")
#     if(line.lower() == "q"):
#         break
#     print(f"you typed: {line}")

###FOR LOOP
numbers = [1,2,3,4,5,]
print(numbers[0])

for batman in numbers:
    print(batman * 3)

total = 0

for number in numbers:
    total = total + number
print(total)

chickens = ["Margaret", "Hetty", "Henrietta", "Audrey", "Mabel"]

for chicken in chickens:
    print(chicken)


chickens = [
    {"name":"Margeretee", "age": 2, "eggs": 0},
    {"name":"Hetty", "age": 4, "eggs": 5},
    {"name":"henriette", "age": 7, "eggs": 1},
    {"name":"audrey", "age": 2, "eggs": 0},
    {"name":"mabel", "age": 2, "eggs": 0},
]

for chicken in chickens:
    print(f'{chicken["name"]} is {chicken["age"]}')


total_eggs = 0

for chicken in chickens:
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0


print(f'{total_eggs} eggs collected')
print(chickens)