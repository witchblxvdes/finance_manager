def calculate_income(transactions: list[dict]) -> float:
    """
    Calculates the total income.

    Args:
        transactions: List of transactions.

    Returns:
        Total amount of income.
    """
    total = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total += transaction["amount"]

    return total

def calculate_expenses(transactions: list[dict]) -> float:
    """
    Calculates the total expenses.

    Args:
        transactions: List of transactions.

    Returns:
        Total amount of expenses.
    """
    total_expenses = 0
    for transaction in transactions:
        if transaction["type"] == "expense":
            total_expenses += transaction["amount"]
    return total_expenses

def calculate_balance(transactions: list[dict]) -> float:
    """
    Calculates the current balance.

    Args:
        transactions: List of transactions.

    Returns:
        Current balance (income minus expenses).
    """
    balance = calculate_income(transactions) - calculate_expenses(transactions)
    return balance

def filter_by_category(transactions: list[dict],
    category: str
) -> list[dict]:
    """
    Filters transactions by category.

    Args:
        transactions: List of transactions.
        category: Category name to filter by.

    Returns:
        List of transactions matching the specified category.
    """
    result = []
    for transaction in transactions:
        if transaction["category"] == category:
            result.append(transaction)
    return result