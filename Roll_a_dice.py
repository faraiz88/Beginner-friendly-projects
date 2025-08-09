import random


while True:
    user = input("Do you want to roll the dice?(y/n): ")

    if user == "y":
        dice = random.randint(1, 6)
        print(f"You rolled at {dice}")
    
    elif user == "n":
        print("Exiting...")
        break

    else:
        print("Please enter a valid input (y/n)")