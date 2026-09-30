# 💰 Simple Python Expense Tracker

A straightforward, beginner-to-intermediate Python project that tracks daily expenses using a local CSV file (`expenses.csv`).

---

## 🎯 What You Learn With This Project

- **File Handling in Python**: Using `with open(...)` and the built-in `csv` module (`csv.DictReader` and `csv.DictWriter`).
- **Data Structures**: Using lists and dictionaries to filter and sum amounts.
- **Functions & Flow Control**: Breaking program logic into small, reusable functions and handling a `while True` loop with user choices.
- **Handling User Input**: Simple `try/except` blocks to handle invalid numeric inputs safely.

---

## 🚀 How to Run It

Open your terminal in this folder and run:

```bash
python3 main.py
```

### Features:
1. **Add Expense**: Enter amount, pick a category (Food, Transport, Rent, etc.), add an optional description, and select a date (defaults to today).
2. **View All Expenses**: Displays a clean text table with all recorded expenses and total amount spent.
3. **Spending Summary**: Calculates total spending and shows the breakdown by category with percentages.
4. **Data Saved to CSV**: Every expense is saved directly to `expenses.csv`, which you can open anytime in Excel, Google Sheets, or Notepad.

---

## 📄 File Overview

- `main.py`: The complete, self-contained application (easy to read and modify).
- `expenses.csv`: Created automatically on first run to store your data.
