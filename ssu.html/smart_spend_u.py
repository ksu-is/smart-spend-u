import csv
import os
from datetime import datetime

DATA_FILE = "smart_spend_u_data.csv"


class Transaction:
    def __init__(self, tid, date, ttype, category, description, amount):
        self.id = tid              # int
        self.date = date           # string YYYY-MM-DD
        self.type = ttype          # "income" or "expense"
        self.category = category   # string
        self.description = description  # string
        self.amount = amount       # float

    def to_row(self):
        return [
            str(self.id),
            self.date,
            self.type,
            self.category,
            self.description,
            f"{self.amount:.2f}",
        ]

    @staticmethod
    def from_row(row):
        tid = int(row[0])
        date = row[1]
        ttype = row[2]
        category = row[3]
        description = row[4]
        amount = float(row[5])
        return Transaction(tid, date, ttype, category, description, amount)


def load_transactions():
    transactions = []
    if not os.path.exists(DATA_FILE):
        return transactions

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            try:
                transactions.append(Transaction.from_row(row))
            except (ValueError, IndexError):
                # Skip corrupted rows
                continue
    return transactions


def save_transactions(transactions):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for t in transactions:
            writer.writerow(t.to_row())


def get_next_id(transactions):
    if not transactions:
        return 1
    return max(t.id for t in transactions) + 1


def input_date(prompt="Enter date (YYYY-MM-DD) or leave blank for today: "):
    while True:
        date_str = input(prompt).strip()
        if date_str == "":
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def input_amount():
    while True:
        amt_str = input("Enter amount: ").strip()
        try:
            amt = float(amt_str)
            if amt <= 0:
                print("Amount must be greater than zero.")
                continue
            return amt
        except ValueError:
            print("Please enter a valid number.")


def add_transaction(transactions, ttype):
    print("\n=== Add", "Income" if ttype == "income" else "Expense", "===")
    date = input_date()
    description = input("Enter description: ").strip()
    category = input("Enter category (Rent, Food, School, etc.): ").strip()
    amount = input_amount()

    tid = get_next_id(transactions)
    new_t = Transaction(tid, date, ttype, category, description, amount)
    transactions.append(new_t)
    print(f"Transaction #{tid} added.\n")


def show_summary(transactions):
    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expenses = sum(t.amount for t in transactions if t.type == "expense")
    balance = total_income - total_expenses

    print("\n=== Budget Summary ===")
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print("-" * 30)
    print(f"Balance:        ${balance:.2f}")
    print()


def list_transactions(transactions):
    if not transactions:
        print("\nNo transactions recorded yet.\n")
        return

    print("\n=== All Transactions ===")
    print(f"{'ID':<4} {'Date':<12} {'Type':<8} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 70)
    for t in sorted(transactions, key=lambda x: (x.date, x.id)):
        sign = "+" if t.type == "income" else "-"
        print(
            f"{t.id:<4} {t.date:<12} {t.type:<8} "
            f"{t.category:<15} {sign}${t.amount:>9.2f}  {t.description}"
        )
    print()


def list_by_category(transactions):
    if not transactions:
        print("\nNo transactions recorded yet.\n")
        return

    category = input("\nEnter category to filter by: ").strip()
    filtered = [t for t in transactions if t.category.lower() == category.lower()]

    if not filtered:
        print(f"\nNo transactions found for category '{category}'.\n")
        return

    print(f"\n=== Transactions in Category: {category} ===")
    print(f"{'ID':<4} {'Date':<12} {'Type':<8} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 70)
    for t in sorted(filtered, key=lambda x: (x.date, x.id)):
        sign = "+" if t.type == "income" else "-"
        print(
            f"{t.id:<4} {t.date:<12} {t.type:<8} "
            f"{t.category:<15} {sign}${t.amount:>9.2f}  {t.description}"
        )
    print()


def delete_transaction(transactions):
    if not transactions:
        print("\nNo transactions to delete.\n")
        return

    list_transactions(transactions)
    id_str = input("Enter the ID of the transaction to delete: ").strip()
    try:
        tid = int(id_str)
    except ValueError:
        print("Invalid ID.\n")
        return

    for t in transactions:
        if t.id == tid:
            confirm = input(f"Are you sure you want to delete transaction #{tid}? (y/n): ").strip().lower()
            if confirm == "y":
                transactions.remove(t)
                print(f"Transaction #{tid} deleted.\n")
            else:
                print("Delete cancelled.\n")
            return

    print(f"No transaction found with ID {tid}.\n")


def main_menu():
    print("======================================")
    print("        Smart Spend U Tracker")
    print("======================================")
    print("1. View budget summary")
    print("2. View all transactions")
    print("3. Add income")
    print("4. Add expense")
    print("5. View transactions by category")
    print("6. Delete a transaction")
    print("7. Save and exit")
    print("======================================")


def main():
    transactions = load_transactions()
    print("Welcome to Smart Spend U!")
    print("Track your student money in one place.\n")

    while True:
        main_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            show_summary(transactions)
        elif choice == "2":
            list_transactions(transactions)
        elif choice == "3":
            add_transaction(transactions, "income")
        elif choice == "4":
            add_transaction(transactions, "expense")
        elif choice == "5":
            list_by_category(transactions)
        elif choice == "6":
            delete_transaction(transactions)
        elif choice == "7":
            save_transactions(transactions)
            print("\nData saved. Goodbye from Smart Spend U!\n")
            break
        else:
            print("Invalid option. Please choose 1–7.\n")


if __name__ == "__main__":
    main()



