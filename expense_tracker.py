import json

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

def add_category():
    category = input("Enter category: ")
    data = load(CATEGORY_FILE)
    if any(item for item in data if item == category):
        print(f"{category} category already exist")
        return
    data.append(category)
    save(data, CATEGORY_FILE)

