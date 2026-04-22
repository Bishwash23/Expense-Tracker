import json
from datetime import datetime

EXPENSE_FILE = "expense.json"
CATEGORY_FILE = "category.json"

def save(data, f):
    with open(f, 'w') as file:
        json.dump(data, file, indent=4)

def load(f):
    try:
        with open(f, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_category(category):
    data = load(CATEGORY_FILE)
    if any(item for item in data if item == category):
        print(f"{category} category already exist")
        return
    data.append(category)
    save(data, CATEGORY_FILE)

def add_expense():
    category_data = load(CATEGORY_FILE)
    print("\nChose one category or create one")
    for c in category_data:
        print(c)
    category = input("Category: ").lower().strip()
    if not category in category_data:
        add_category(category)
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Invalid amount")
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M")
    data = load(EXPENSE_FILE)
    data.append({"category":category, "amount":amount, "date":date, "time":time})
    save(data, EXPENSE_FILE)

def monthly_summary():
    month = input("\nEnter month (YYYY-MM): ")
    data = load(EXPENSE_FILE)

    total = 0
    for exp in data:
        if exp["date"].startswith(month):
            total += exp["amount"]
    
    print("Total expense: ", total)

def filter():
    print("\nFilter by:\n1. Date\n2. Category")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            month_filter()
        case 2:
            category_filter()
        case _:
            print("Invalid choice")

def month_filter():
    month = input("\nEnter month (YYYY-MM): ")
    data = load(EXPENSE_FILE)
    
    for exp in data:
        if exp["date"].startswith(month):
            print(f"{exp["category"]} | {exp["amount"]} | {exp["date"]}")

def category_filter():
    category = input("\nEnter category: ")
    data = load(EXPENSE_FILE)

    for exp in data:
        if exp["category"] == category:
            print(f"{exp["category"]} | {exp["amount"]} | {exp["date"]}")

def view_expenses():
    data = load(EXPENSE_FILE)
    for exp in data:
        print(f"{exp["category"]} | {exp["amount"]} | {exp["date"]}")

def category_summary():
    category = input("\nEnter category: ")
    data = load(EXPENSE_FILE)

    total = 0
    for exp in data:
        if exp["category"] == category:
            total += exp["amount"]
    print("Total expense: ", total)

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Filter")
        print("4. Monthly Summary")
        print("5. Category Summary")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        match choice:
            case 1:
                add_expense()
            case 2:
                view_expenses()
            case 3:
                filter()
            case 4:
                monthly_summary
            case 5:
                category_summary()
            case 6:
                print("Exiting...")
                break
            case _:
                print("Invalid choice")

main()