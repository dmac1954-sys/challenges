from datetime import datetime
from src.transaction import Transaction
from src.findb import (
    view_statement,
    create_connection,
    filter_statement,
    view_categories,
    set_budget,
    budget_viewer,
    generate_report
)

DB_PATH = "/workspaces/challenges/finance/finance.db"


def main():
    while True:
        print("1. Add a transaction")
        print("2. View statement")
        print("3. Budgets")
        print("4. Quit the program")
        user_choice = input("Enter: ")
        if user_choice == "4":
            break
        elif user_choice == "1":
            while True:
                input_type = input("Type (Income or Expense): ")
                input_type = input_type.strip().title()
                if is_valid_type(input_type):
                    break
            while True:
                input_amount = input("Amount: ")
                if is_valid_amount(input_amount):
                    break
            while True:
                input_date = input("Date [yyyy-mm-dd]: ")
                if is_valid_date(input_date):
                    break
            input_category = input("Category ID: ")
            input_description = input("Description: ")

            t = Transaction(
                input_type, input_amount, input_date, input_category, input_description
            )
            t.update_db()

        elif user_choice == "2":
            print("1. View all transactions")
            print("2. Filter transactions by category")
            option = input("Enter: ")
            if option == "1":
                conn = create_connection(DB_PATH)
                with conn:
                    transactions = view_statement(conn)
                print("Type", "Amount", "Date", "Category", "Description")
                for transaction in transactions:
                    print(
                        transaction[0],
                        transaction[1],
                        transaction[2],
                        transaction[3],
                        transaction[4],
                    )
            elif option == "2":
                conn = create_connection(DB_PATH)
                with conn:
                    categories = view_categories(conn)
                print("ID", "Category")
                for category in categories:
                    print(category[0], category[1])
                filter = input("Enter ID: ")
                with conn:
                    results = filter_statement(conn, filter)
                print("Type", "Amount", "Date", "Description")
                for result in results:
                    print(result[0], result[1], result[2], result[3])

        elif user_choice == "3":
            conn = create_connection(DB_PATH)
            print("1. Set up a budget")
            print("2. View all budgets")
            print("3. Budget report")
            print("4. Return to main menu")
            budget_option = input("Enter: ")
            if budget_option == "1":
                print("Select a category you want to set up a budget for")
                with conn:
                    categories = view_categories(conn)
                print("ID", "Category")
                for category in categories:
                    print(category[0], category[1])
                category_choice = input("Enter ID: ")
                while True:
                    budget_amount = input("Enter amount: ")
                    if is_valid_amount(budget_amount):
                        budget_amount = float(budget_amount)
                        break
                with conn:
                    transaction = (category_choice, budget_amount)
                    set_budget(conn, transaction)

            elif budget_option == "2":
                with conn:
                    budgets = budget_viewer(conn)
                print("ID", "Amount")
                for budget in budgets:
                    print(budget[0], budget[1])

            elif budget_option == "3":
                with conn:
                    report_entries = generate_report(conn)
                print("Category", "Expenditure", "Budget")
                for entry in report_entries:
                    print(entry[0], entry[1], entry[2])
                    if entry[1] > entry[2]:
                        print("(Warning! You are over the set budget!)")
                
            # print(f"Type: {input_type}")
            # print(f"Amount: {input_amount}")
            # print(f"Date: {input_date}")
            # print(f"Category: {input_category}")
            # print(f"Description: {input_description}")


def is_valid_type(input_type):
    if input_type == "Income" or input_type == "Expense":
        return True
    return False


def is_valid_amount(input_amount):
    try:
        input_amount = float(input_amount)
        if len(str(input_amount).split(".")[1]) > 2 or input_amount < 0:
            raise ValueError
        return True
    except ValueError:
        return False


def is_valid_date(input_date):
    try:
        datetime.strptime(input_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
