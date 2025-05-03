import sqlite3 as db
from datetime import datetime

def init():
    '''
    Initialize a new database with users and expenses tables
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            amount REAL,
            category TEXT,
            message TEXT,
            date TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')

    conn.commit()
    conn.close()


def register_user(username, password):
    '''
    Register a new user with the specified username and password
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()

    # Check if the user already exists
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cur.fetchone():
        print("User already exists.")
        return False

    # Insert the new user into the users table
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    return True

def login_user(username, password):
    '''
    Log in a user by checking if the username and password match
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    if cur.fetchone():
        return True
    return False

def log(username, amount, category, message=""):
    '''
    Log the expenditure in the database
    '''
    date = str(datetime.now())
    data = (username, amount, category, message, date)
    conn = db.connect("spent.db")
    cur = conn.cursor()
    sql = 'INSERT INTO expenses (username, amount, category, message, date) VALUES (?, ?, ?, ?, ?)'
    cur.execute(sql, data)
    conn.commit()

def view(username, category=None):
    '''
    View the expenses for a user and return the total
    '''
    conn = db.connect("spent.db")
    cur = conn.cursor()

    if category:
        sql = '''
        SELECT * FROM expenses WHERE username = ? AND category = ?
        '''
        cur.execute(sql, (username, category))
    else:
        sql = '''
        SELECT * FROM expenses WHERE username = ?
        '''
        cur.execute(sql, (username,))
    
    results = cur.fetchall()

    # Get the total expense
    sql_total = '''
    SELECT SUM(amount) FROM expenses WHERE username = ?
    '''
    cur.execute(sql_total, (username,))
    total_amount = cur.fetchone()[0]

    return total_amount, results

def export_to_csv(username, filename="expenses.csv", category=None, start_date=None, end_date=None):
    '''
    Export expenses to a CSV file
    '''
    import csv
    conn = db.connect("spent.db")
    cur = conn.cursor()

    query = '''
    SELECT * FROM expenses WHERE username = ?
    '''
    params = [username]

    if category:
        query += ' AND category = ?'
        params.append(category)
    
    if start_date:
        query += ' AND date >= ?'
        params.append(start_date)
    
    if end_date:
        query += ' AND date <= ?'
        params.append(end_date)

    cur.execute(query, tuple(params))
    results = cur.fetchall()

    # Write to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Username", "Amount", "Category", "Message", "Date"])
        for row in results:
            writer.writerow(row)

    # Return the filename and number of records exported
    return filename, len(results), sum([row[2] for row in results]) if results else 0
