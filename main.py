from transactions import (
    add_transaction,
    show_transactions,
    delete_transaction
)

from statistics import (
    calculate_income,
    calculate_expenses,
    calculate_balance,
    filter_by_category
)


transactions = []


def show_menu() -> None:
    """
    Displays the main program menu.

    Returns:
        None.
    """
    print("\n========== PERSONAL FINANCE MANAGER ==========")
    print("1. Add income")
    print("2. Add expense")
    print("3. Show all transactions")
    print("4. Show total income")
    print("5. Show total expenses")
    print("6. Show balance")
    print("7. Filter by category")
    print("8. Delete transaction")
    print("0. Exit")


def main() -> None:
    """
    Runs the main program loop.

    Displays the menu and processes user choices until
    the user selects the exit option.

    Returns:
        None.
    """
    while True:
        show_menu()

        choice = input("\nChoose an action: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            add_transaction(
                transactions,
                "income",
                amount,
                category,
                description
            )

            print("Income added successfully!")

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            add_transaction(
                transactions,
                "expense",
                amount,
                category,
                description
            )

            print("Expense added successfully!")

        elif choice == "3":
            show_transactions(transactions)

        elif choice == "4":
            income = calculate_income(transactions)
            print(f"Total income: {income}")

        elif choice == "5":
            expenses = calculate_expenses(transactions)
            print(f"Total expenses: {expenses}")

        elif choice == "6":
            balance = calculate_balance(transactions)
            print(f"Current balance: {balance}")

        elif choice == "7":
            category = input("Enter category: ")

            result = filter_by_category(transactions, category)

            show_transactions(result)

        elif choice == "8":
            transaction_id = int(input("Enter transaction ID: "))

            delete_transaction(transactions, transaction_id)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()