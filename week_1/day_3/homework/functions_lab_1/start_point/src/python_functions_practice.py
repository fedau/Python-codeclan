def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


def length_of_string(str):
    return len(str)


def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(str1, str2):
    return int(str1) + int(str2)

def number_to_full_month_name(month):
    months = { 
        1: "January",
        2: "Febuary",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",

    }
    return months[month]

def number_to_short_month_name(month):
    months = { 
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",

    }
    return months[month]

def cube_volume(length):
    return length ** 3


def random(word):
    # index = len(word) -1
    # for 
    # return word.reverse(word)
    return word[::-1]

def convert(numb):
    return (numb - 30) /2