import json
import os

FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):

    print("\n--- Add Expense ---")

    category = input("Category: ")

    while True:
        try:
            amount = float(input("Amount: "))
            break

        except ValueError:
            print("Please enter a valid amount.")


    description = input("Description: ")

    date = input("Date (DD-MM-YYYY): ")


    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }


    expenses.append(expense)

    save_expenses(expenses)

    print("\n✅ Expense added successfully!")


# Display all expenses
def view_expenses(expenses):

    print("\n====== ALL EXPENSES ======")


    if not expenses:
        print("No expenses found.")
        return


    for index, expense in enumerate(expenses, start=1):

        print(f"""
Expense No: {index}
Category: {expense['category']}
Amount: ₹{expense['amount']}
Description: {expense['description']}
Date: {expense['date']}
--------------------------
""")


# Calculate total spending
def show_total(expenses):

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(f"\n💰 Total Spending: ₹{total}")


# Main program
def main():

    expenses = load_expenses()


    print("""
=============================
     💰 EXPENSE TRACKER
=============================

Track your expenses.
Manage your money better.
""")


    while True:

        print("""
------------ MENU ------------

1. ➕ Add Expense
2. 📋 View Expenses
3. 📊 Show Total
4. 🚪 Exit

-------------------------------
""")


        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Enter a number only.")
            continue


        if choice == 1:

            add_expense(expenses)


        elif choice == 2:

            view_expenses(expenses)


        elif choice == 3:

            show_total(expenses)


        elif choice == 4:

            save_expenses(expenses)

            print("""
================================

Thank you for using Expense Tracker!

Your data is saved safely.
See you again! 👋

================================
""")

            break


        else:

            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()