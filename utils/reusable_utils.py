import random

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]


def generate_random_name():
    name = ""
    for i in range(7):
        name = name + letters[random.randint(0, 11)]

    return name

def generate_random_username():
    name = ""
    for i in range(3):
        name = name + letters[random.randint(0, 11)]

    return name + "Test"

def generate_random_email():
    email = ""
    for i in range(7):
        email = email + letters[random.randint(0, 11)]

    email = email + "@" + domains[random.randint(0, 5)]
    return email


print(generate_random_name())
print(generate_random_email())
