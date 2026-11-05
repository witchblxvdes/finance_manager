
## 1. Project Name

Finance Manager

## 2. Program Purpose

Finance Manager is a simple console-based Python application designed to manage personal finances.

The program allows users to track their income and expenses, view their current balance, and organize transactions by category.

## 3. Main Features

- Add income transactions.
- Add expense transactions.
- Display all transactions.
- Delete transactions by ID.
- Calculate total income.
- Calculate total expenses.
- Calculate current balance.
- Filter transactions by category.
- Automatically generate unique transaction IDs.
- Validate transaction data.

## 4. Project Structure

```text
finance_manager/
│
├── main.py
├── transactions.py
├── statistics.py
├── README.md
└── .gitignore
```

### File Description

- `main.py` — Main application file containing the console menu.
- `transactions.py` — Functions for adding, displaying, and deleting transactions.
- `statistics.py` — Functions for calculating financial statistics and filtering transactions.
- `README.md` — Project documentation.
- `.gitignore` — Files and directories ignored by Git.

## 5. How to Run

### Requirements

- Python 3.9 or newer.
- Git (optional, for cloning the repository).

### Installation and Launch

1. Clone the repository:

   ```bash
   git clone https://github.com/witchblxvdes/finance_manager.git
   ```

2. Open the project directory:

   ```bash
   cd finance_manager
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## 6. Usage Examples

After launching the program, the following menu will appear:

```text
========== FINANCE MANAGER ==========

1. Add income
2. Add expense
3. Show all transactions
4. Show total income
5. Show total expenses
6. Show balance
7. Filter by category
8. Delete transaction
0. Exit
```

### Example: Adding Transactions

```text
Choose an action: 1
Enter income amount: 15000
Enter category: Salary
Enter description: Monthly salary

Income added successfully!
```

```text
Choose an action: 2
Enter expense amount: 2500
Enter category: Food
Enter description: Groceries

Expense added successfully!
```

### Example: Displaying Transactions

```text
ID | TYPE | AMOUNT | CATEGORY | DESCRIPTION
------------------------------------------------
1 | income | 15000 | Salary | Monthly salary
2 | expense | 2500 | Food | Groceries
```

### Example: Financial Statistics

```text
Total income: 15000
Total expenses: 2500
Current balance: 12500
```

### Example: Filtering by Category

```text
Choose an action: 7
Enter category: Food

ID | TYPE | AMOUNT | CATEGORY | DESCRIPTION
------------------------------------------------
2 | expense | 2500 | Food | Groceries
```

### Example: Deleting a Transaction

```text
Choose an action: 8
Enter transaction ID: 2

Transaction deleted successfully.
```

## Data Storage

Transactions are stored in an in-memory Python list.
All transaction data is lost when the application is closed.

Temporary change for Git revert demonstration.