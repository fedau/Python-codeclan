# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# 2. Print the difference between the largest and smallest value:
min_val = min(numbers)
max_val = max(numbers)
difference = max_val - min_val
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
result = False
index = 0
for number in numbers:
    if (number == 2 and numbers[index-1] == 2):
        result = True
    index += 1
print(result)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

total = 0 
found_6 = False
for number in numbers:
    if number == 6:
        found_6 = True
    elif found_6:
        if number == 7:
            found_6 = False
    else:
         total += number
print(total)



# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# total = 0

# indices_of_13 = []
# counter = 0
# for num in numbers:
#     if num ==13:
#         indices_of_13.append(num)
#         counter += 1
#     elif len(indices_of_13) != 0 and (indices_of_13[-1] == counter -1):
#         counter  += 1
#         pass
# else:
#         total += num
#         counter += 1



index = 0
total = 0
for number in numbers:
    if number == 13 or numbers[index-1] == 13:
        pass
    else:
        total += number
    index += 1
print(total)










#MY TRIES
# while (numbers != 13):

# for number in numbers != 13:
#     total = total + number
# print(total)


# for number in numbers:
#     if number != 13:
#         print(num)