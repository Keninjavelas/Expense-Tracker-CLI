# Expense-Tracker-CLI
A simple, multi-user command-line expense tracker built with Python and SQLite.
## 🚀 Features

- User registration & login
- Log expenses by category
- View expenses with optional filters
- Export expenses to CSV
- Password-protected access
- Date filtering for exports


## 📁 Project Structure

* **`spent.py`** – Core logic for:
  * Initializing the database
  * Logging and viewing expenses
  * Exporting data to CSV
  * User registration and login
* **`spent_driver.py`** – Command-line interface using `argparse`; acts as the main entry point for user commands
* **`reset_db.py`** – Utility script to delete and recreate the database with the correct schema
* **`spent.db`** – SQLite database file (auto-generated)
* **`requirements.txt`** – List of required Python packages (`tabulate`)
* **`.gitignore`** – Tells Git which files/folders to ignore (e.g., `.db`, `venv/`, `__pycache__/`)
* **`README.md`** – Project documentation and usage instructions

