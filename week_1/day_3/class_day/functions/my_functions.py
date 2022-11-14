
#simpel print function
# def greet():
#     print("Hey")

# greet()

#function with variable and return
# def greetReturn():
#     return "Hey Return"

# greeting = greetReturn()
# print(greeting)

# greetReturn()


# #a parameter function

# def greetParam(name):
#     return "Hey " + name

# greetingFedau = greetParam("Fedau")
# print(greetingFedau)


# #multiple parameters

# def day(name, time_of_day):
#     return "Good " + time_of_day + ", " + name
# daytime = day("Fedau", "Afternoon")

# print(daytime)


# def hiya()
# def greet(name, time_of_day)

# name_1 = "Fee"
# timeOfday = "morning"

# name_2 = "ben"
# timeOfday2 = "afternoon"
# greeting = greet(name_1, timeOfday)
# greeting = greet(name_2, timeOfday2)
# print(greeting)


# def greet():
#     words = "hey"
#     return words

# def greet_two():
#     words = "whut"
#     return words
# print(greet_two())



chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs(list):
    
    total_eggs = 0

    for bird in list:
        total_eggs += bird["eggs"]
        bird["eggs"] = 0 # eggs have been collected

    return (f"{total_eggs} eggs collected")

print(count_eggs(chickens))