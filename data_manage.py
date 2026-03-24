import json
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expense(expense):
    expenses = load_expenses()
    expenses.append(expense)
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=2)

def get_expenses_by_category():
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]
    return summary
