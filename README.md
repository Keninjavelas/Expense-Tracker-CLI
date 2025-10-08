
# 💰 Expense Tracker CLI

A **lightweight**, **multi-user command-line expense tracker** built with **Python** and **SQLite**.
Easily log, view, and export expenses — all from your terminal.

---

## 🚀 Features

* 👤 **User Registration & Login** — password-protected access for multiple users
* 🧾 **Log Expenses by Category** — organize spending efficiently
* 🔍 **View Expenses** — filter by date, category, or amount
* 📤 **Export to CSV** — backup or analyze your expenses externally
* 🔒 **Secure Access** — each user’s data is isolated and protected
* 🗓️ **Date-Based Filtering** — narrow down expenses for reports or exports

---

## 📁 Project Structure

```
Expense-Tracker-CLI/
├── spent.py          # Core logic: DB setup, expense logging/viewing, CSV export, user auth
├── spent_driver.py   # CLI interface using argparse (main entry point)
├── reset_db.py       # Utility to reset and recreate the database schema
├── spent.db          # SQLite database file (auto-generated)
├── requirements.txt  # Python dependencies (e.g., tabulate)
├── .gitignore        # Ignore venv, cache, and DB files
└── README.md         # You're here!
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** SQLite
* **CLI Framework:** argparse
* **Dependencies:** tabulate

---

## ⚙️ Setup & Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Expense-Tracker-CLI.git
   cd Expense-Tracker-CLI
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tracker**

   ```bash
   python spent_driver.py
   ```

4. **Example commands**

   ```bash
   python spent_driver.py register        # Create a new user
   python spent_driver.py login           # Log in as an existing user
   python spent_driver.py add             # Add a new expense
   python spent_driver.py view            # View expenses (with filters)
   python spent_driver.py export          # Export data to CSV
   ```

---

## 🔄 Resetting the Database

If you need to start fresh, run:

```bash
python reset_db.py
```

This deletes and recreates the `spent.db` file with a clean schema.

---

## 💡 Future Improvements

* 📊 Add per-user expense summaries and stats
* 🔐 Password hashing for enhanced security
* ☁️ Optional cloud backup integration
* 🧮 Support for recurring expenses

---

## 📜 License

This project is open-source and available under the **MIT License**.


