import csv
import os
from datetime import date

# The CSV file where expenses will be saved
FILE_NAME = "expenses.csv"
COLUMNS = ["Date", "Category", "Amount", "Description"]


def initialize_file():
    """Create the CSV file with headers if it does not exist yet."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=COLUMNS)
            writer.writeheader()


def add_expense():
    """Ask user for expense details and save to CSV file."""
    print("\n--- Add New Expense ---")

    # 1. Get amount with simple validation
    while True:
        amount_input = input("Enter amount ($): ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number (e.g., 15.50).")

    # 2. Category selection
    categories = ["Food", "Transport", "Rent", "Bills", "Entertainment", "Other"]
    print("\nSelect Category:")
    for index, cat in enumerate(categories, start=1):
        print(f"  {index}. {cat}")

    while True:
        cat_choice = input(f"Choose (1-{len(categories)}) or type custom: ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        elif cat_choice:
            category = cat_choice
            break

    # 3. Description
    description = input("Enter description (e.g., lunch, groceries): ").strip()
    if not description:
        description = "N/A"

    # 4. Date (default to today)
    today = date.today().strftime("%Y-%m-%d")
    date_input = input(f"Enter date (YYYY-MM-DD) [Press Enter for today: {today}]: ").strip()
    expense_date = date_input if date_input else today

    # 5. Append to CSV file
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writerow({
            "Date": expense_date,
            "Category": category,
            "Amount": f"{amount:.2f}",
            "Description": description,
        })

    print(f"\n Expense added: ${amount:.2f} for '{category}' on {expense_date}!\n")


def view_expenses():
    """Read and display all expenses from the CSV file."""
    print("\n--- All Expenses ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    # Print a simple, clean table
    print(f"{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 55)

    total = 0.0
    for row in rows:
        amount = float(row["Amount"])
        total += amount
        print(f"{row['Date']:<12} | {row['Category']:<15} | ${amount:<9.2f} | {row['Description']}")

    print("-" * 55)
    print(f"Total Spent: ${total:.2f} ({len(rows)} entries)\n")


def view_summary():
    """Calculate and show total spent per category."""
    print("\n--- Spending Summary by Category ---")

    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.\n")
        return

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    # Sum spending by category using a dictionary
    totals_by_category = {}
    grand_total = 0.0

    for row in rows:
        category = row["Category"]
        amount = float(row["Amount"])
        totals_by_category[category] = totals_by_category.get(category, 0.0) + amount
        grand_total += amount

    # Display totals
    for category, total in totals_by_category.items():
        percentage = (total / grand_total) * 100
        print(f" • {category:<15}: ${total:>8.2f}  ({percentage:.1f}%)")

    print("-" * 45)
    print(f" Grand Total     : ${grand_total:>8.2f}\n")


def main():
    """Main program loop."""
    initialize_file()

    while True:
        print("==============================")
        print("   PERSONAL EXPENSE TRACKER   ")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Spending Summary")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("\nGoodbye! Have a great day!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
