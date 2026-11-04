def calculate_income(transactions):
    total = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total += transaction["amount"]

    return total

def calculate_expenses(transactions):
    total_expenses = 0
    for transaction in transactions:
        if transaction["type"] == "expense":
            total_expenses += transaction["amount"]
    return total_expenses

def calculate_balance(transactions):
    balance = calculate_income(transactions) - calculate_expenses(transactions)
    return balance

def filter_by_category(transactions, category):
    result = []
    for transaction in transactions:
        if transaction["category"] == category:
            result.append(transaction)
    return result