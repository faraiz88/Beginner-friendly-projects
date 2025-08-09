import json
import os


FILENAME = "expenses.json"

def save_expenses_to_file():
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent = 4)

def load_expenses_from_file():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
        
    return []
expenses = load_expenses_from_file()


def show_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show by Category")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        amount = int(input("Enter amount: "))
        category = input("Enter Category: ")
        date = input("Enter a date(YYYY-MM-DD): ")
        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        print(f"Spent: {amount} for {category} on {date}")
        save_expenses_to_file()

    
    elif choice == "2":
        if not expenses:
            print("No expense recorded yet.")
        else:
            for e in expenses:
                print(f"spent: ₹{e['amount']} for {e['category']} on {e['date']}")
    
    elif choice == "3":
        total = 0
        for e in expenses:
            total += e['amount']
        print(f"Total spent: ₹{total}")
    
    elif choice == "4":
        if not expenses:
            print("No expense to show by category.")
        else:
            category_total = {}
            for e in expenses:
                cat = e['category']
                amt = e['amount']
                if cat in category_total:
                    category_total[cat] += amt
                else:
                    category_total[cat] = amt
            
            print("\nExpenses by Category:")
            for cat, total in category_total.items():
                print(f"{cat}: ₹{total}")
    
    elif choice == "5":
        print("Exiting...")
        break


