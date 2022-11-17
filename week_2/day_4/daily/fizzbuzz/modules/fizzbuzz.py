def fizzbuzz(num):
    divisibility_by_3 = num % 3 == 0 
    divisibility_by_5 = num % 5 == 0 
    if divisibility_by_3 and divisibility_by_5:
        return "Fizzbuzz"
    elif divisibility_by_3:
        return "Fizz"
    elif divisibility_by_5:
        return "buzz"
    else:
        return f"{num}"