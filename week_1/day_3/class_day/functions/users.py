users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]

# write function that can find a user in the list by user_id

def user_by_id(users_list, users_id):
    for user in users_list:
        if user["user_id"] == users_id:
            return user
    return None

desired_id = input('Please enter the desired user ID> ')
desired_id = int(desired_id)

user = user_by_id(users, desired_id)
print(user)