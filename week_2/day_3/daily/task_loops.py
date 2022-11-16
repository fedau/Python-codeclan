# ages = [5, 15, 64, 27, 84, 26]
# odd_ages = []

# for age in ages:
#     if age % 2 != 0:
#         odd_ages.append(age)

ages = [5, 15, 64, 27, 84, 26,]
odd_ages = [age for age in ages if age % 2 != 0]

print(odd_ages)


chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

long_names =[name for name in chicken_names if len(name) > 10]
print(long_names)

h_names =[name for name in chicken_names if name[0] == "H"]
print(h_names)


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

first_letter = [letter[0].lower() for letter in words]
print(first_letter)