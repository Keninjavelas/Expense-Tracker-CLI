import argparse
from spent import init, register_user, login_user, log, view, export_to_csv

def main():
    init()

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Register
    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("username")
    register_parser.add_argument("password")

    # Login
    login_parser = subparsers.add_parser("login", help="Login as a user")
    login_parser.add_argument("username")
    login_parser.add_argument("password")

    # Log expense
    log_parser = subparsers.add_parser("log", help="Log a new expense")
    log_parser.add_argument("username")
    log_parser.add_argument("amount", type=float)
    log_parser.add_argument("category")
    log_parser.add_argument("message", nargs="?", default="")

    # View expenses
    view_parser = subparsers.add_parser("view", help="View your expenses")
    view_parser.add_argument("username")
    view_parser.add_argument("--category", help="Optional category filter")

    # Export to CSV
    export_parser = subparsers.add_parser("export", help="Export expenses to CSV")
    export_parser.add_argument("username")
    export_parser.add_argument("--category", help="Optional category filter")
    export_parser.add_argument("--start_date", help="Start date (YYYY-MM-DD)", default=None)
    export_parser.add_argument("--end_date", help="End date (YYYY-MM-DD)", default=None)
    export_parser.add_argument("--file", help="Output CSV filename", default="expenses.csv")

    args = parser.parse_args()

    # Handle commands
    if args.command == "register":
        if register_user(args.username, args.password):
            print(f"✅ User '{args.username}' registered successfully.")
        else:
            print(f"⚠️ User '{args.username}' already exists.")

    elif args.command == "login":
        if login_user(args.username, args.password):
            print(f"🔓 Login successful. Welcome, {args.username}!")
        else:
            print("❌ Login failed. Invalid username or password.")

    elif args.command == "log":
        log(args.username, args.amount, args.category, args.message)
        print(f"💾 Logged {args.amount} in '{args.category}' for user '{args.username}'.")

    elif args.command == "view":
        total, results = view(args.username, args.category)
        print(f"🧾 Total expense: {total}")
        for row in results:
            print(row)

    elif args.command == "export":
        filename, count, total = export_to_csv(
            args.username,
            args.file,
            args.category,
            args.start_date,
            args.end_date
        )
        print(f"📁 Exported {count} entries (Total: {total}) to '{filename}'.")

if __name__ == "__main__":
    main()
