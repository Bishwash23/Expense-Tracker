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
    print("Chose one category or create one")
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


