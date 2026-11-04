def add_transaction(
    transactions: list[dict],
    transaction_type: str,
    amount: float,
    category: str,
    description: str
) -> list[dict]:
    """
    Adds a new transaction to the transaction list.

    Args:
        transactions: List of existing transactions.
        transaction_type: Transaction type (income or expense).
        amount: Transaction amount.
        category: Transaction category.
        description: Transaction description.

    Returns:
        Updated list of transactions.

    Raises:
        ValueError: If the transaction data is invalid.
    """
    transaction_id = len(transactions) + 1

    if transaction_type not in ["income", "expense"]:
        raise ValueError("Wrong operation type.")

    if amount <= 0:
        raise ValueError("Amount can't be negative or zero.")

    if not category or not description:
        raise ValueError("Category or description can't be empty.")

    transaction = {
        "id": transaction_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description
    }

    transactions.append(transaction)

    return transactions


def show_transactions(transactions: list[dict]) -> None:
    """
    Displays all transactions in a table format.

    Args:
        transactions: List of transactions to display.

    Returns:
        None.
    """
    if not transactions:
        print("No transactions found.")
        return

    print("ID | TYPE | AMOUNT | CATEGORY | DESCRIPTION")
    print("------------------------------------------------")

    for transaction in transactions:
        print(f"{transaction['id']} | {transaction['type']} | {transaction['amount']} | {transaction['category']} | {transaction['description']}")


def delete_transaction(transactions: list[dict],
    transaction_id: int
) -> None:
    """
    Deletes a transaction by its ID.

    Args:
        transactions: List of transactions.
        transaction_id: ID of the transaction to delete.

    Returns:
        None.

    If the transaction is not found, displays an error message.
    """
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            return

    print("Transaction doesn't exist")