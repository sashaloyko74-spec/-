from data_manager import save_expense, load_expenses, get_expenses_by_category
from utils import input_amount, input_category
from datetime import datetime

def add_expense():
    amount = input_amount()
    category = input_category()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense = {"amount": amount, "category": category, "date": date}
    save_expense(expense)
    print("Расход добавлен!")

def show_expenses():
    expenses = load_expenses()
    if not expenses:
        print("Нет расходов")
        return
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | {exp['amount']}")

def show_summary():
    summary = get_expenses_by_category()
    if not summary:
        print("Нет расходов")
        return
    print("Статистика по категориям:")
    for cat, amount in summary.items():
        print(f"{cat}: {amount}")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Статистика по категориям")
        print("4. Выход")
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
