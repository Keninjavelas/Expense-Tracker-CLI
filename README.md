# Expense-Tracker-CLI
A simple, multi-user command-line expense tracker built with Python and SQLite.
## 🚀 Features

- User registration & login
- Log expenses by category
- View expenses with optional filters
- Export expenses to CSV
- Password-protected access
- Date filtering for exports

## 📂 Project Structure
expense-tracker/
│
├── spent.py            → Handles database operations: init, log, view, export, and authentication
├── spent_driver.py     → Command-line interface using argparse (main entry point)
├── reset_db.py         → Resets the database by deleting and recreating it with the correct schema
│
├── spent.db            → The SQLite database (auto-generated after first use)
│
├── requirements.txt    → List of required Python packages
├── .gitignore          → Specifies files/folders Git should ignore (e.g., .db, venv, pycache)
└── README.md           → Project documentation (you're reading it!)
