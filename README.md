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
├── spent.py # Core logic (DB, logging, view, auth, export)
├── spent_driver.py # CLI interface using argparse
├── reset_db.py # Utility script to reset the database
├── spent.db # (Auto-generated) SQLite database
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore # Ignore DB and pycache
