import json
import os

FILENAME = "contacts.json"

def create_function():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        l = []
        with open(FILENAME, "w") as f:
            json.dump(l, f, indent = 4)
            return l
contacts = create_function()
print(contacts)


def contact_details():
    name = input("Enter your name: ")
    phone = input('Enter your phone: ')
    email = input('Enter your email: ')

    contact  = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)

    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent = 4)

while True:
    contact_details()
    more = input("Add another contact? (Y/N): ")
    if more == "n":
        break