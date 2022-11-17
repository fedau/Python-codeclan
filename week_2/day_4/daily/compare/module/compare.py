def compare(user, computer):
    if user > computer:
        return f"{user} is greater than my number"
    if user < computer:
        return f"{user} is less than my number"

    if user == computer:
        return f"{user} is the same as my number"