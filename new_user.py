#!/usr/bin/env python3

import time
import csv
import webbrowser
import random, string

# Dictionary of clients that use JC -
# Add company name as Key in caps, then email domain as value
clients = {
    "BLUEPRINT": "@blueprintpictures.com",
    "CREATURE": "@creaturelondon.com",
    "HEREDESIGN": "@heredesign.co.uk",
    "PAGE&PAGE": "@pageandpage.uk.com",
    "RANKIN": "@rankin.co.uk",
    "WILDCARD": "@wildcard.co.uk",
}

# Three globabl variables, take input to get First Name, Last Name & Client
# company variable is set during function call for client_check()
first_name = input("Please type in the first name for the user: ").capitalize()
last_name = input("Please type in the last name for the user: ").capitalize()
company = ""

# Function to asks input and checks that client name
# from company input exsists in 'Clients' - loops function if company not found
def client_check():
    global company
    company = input("Please enter in the client name: ").replace(" ", "")
    client = company.upper()
    if client in clients.keys():
        client = clients.get(company.upper())
    else:
        print(
            """\nCompany not found, or is not curerntly in App directory.
Please try another company or re-enter to try again.\n"""
        )
        return client_check()
    return client

# Calls function and assigns client value to variable
client_name = client_check()


# Creates a random password of random characters
def password_makerer():
    password_length = 6
    possible_letters = "abcdefghijklmnopqrstuvwxyz"
    possible_nums = "1234567890"
    possible_chars = "!*#"
    random_letter_list = [
        random.choice(possible_letters) for i in range(password_length)
    ]
    random_num_list = [random.choice(possible_nums) for i in range(1)]
    random_chars_list = [random.choice(possible_chars) for i in range(1)]
    random_character_list = (
        random_letter_list + random_num_list + random_chars_list
    )
    random_password = "".join(random_character_list)
    return random_password


# Simple function to create a user email which is firstname@
def first_name_email():
    user_email = (first_name + client_name).lower()
    return user_email


# Functions to create specific client format username & email
def blue_print_user():
    new_user["username"] = (first_name + "." + last_name).lower()
    new_user["email"] = (first_name + "." + last_name + client_name).lower()
    return new_user


def creature_user():
    new_user["username"] = (first_name).lower()
    new_user["email"] = (first_name + last_name[0] + client_name).lower()
    return new_user


def here_user():
    new_user["username"] = (first_name).lower()
    new_user["email"] = first_name_email()
    return new_user


def page_user():
    new_user["username"] = (first_name).lower()
    new_user["email"] = first_name_email()
    return new_user


def rankin_user():
    user_name = (first_name).lower()
    new_user["email"] = first_name_email()
    # user_password = (first_name[0] + last_name[0]).lower() + 'RP' +
    new_user["username"] = user_name
    new_user["email"] = user_email
    return new_user


def wildcard_user():
    new_user["username"] = (first_name + "." + last_name).lower()
    new_user["email"] = (first_name + "." + last_name + client_name).lower()
    return new_user


# User details collated into a dictionary to be exported to CSV
new_user = {
    "firstname": first_name,
    "lastname": last_name,
    "username": "",
    "email": "",
    "password": password_makerer(),
}

# Runs specific function based on input for company / client
if company.upper() == "BLUEPRINT":
    user = [blue_print_user()]
elif company.upper() == "CREATURE":
    user = [creature_user()]
elif company.upper() == "HEREDESIGN":
    user = [here_user()]
elif company.upper() == "PAGE&PAGE":
    user = [page_user()]
elif company.upper() == "RANKIN":
    user = [rankin_user()]
elif company.upper() == "WILDCARD":
    user = [wildcard_user()]


# Creates and writes output of the funtion: user to a CSV
with open("jumpcloud_user.csv", "w") as jumpcloud_user:
    fields = ["firstname", "lastname", "username", "email", "password"]
    output = csv.DictWriter(jumpcloud_user, fieldnames=fields)
    output.writeheader()

    for item in user:
        output.writerow(item)

# Confirmation CSV is created and then launches webbrowser on Jumpcloud login page
print("Jumpcloud User CSV Created Ya Fool!")
time.sleep(1)
webbrowser.open("https://console.jumpcloud.com/login")
