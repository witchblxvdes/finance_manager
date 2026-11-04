def add_transaction(transactions, transaction_type, amount, category, description):
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