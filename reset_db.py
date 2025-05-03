import os
from spent import init

DB_FILE = "spent.db"

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"🗑️ Deleted old '{DB_FILE}'")
else:
    print(f"ℹ️ No existing '{DB_FILE}' found")

init()
print("✅ New database created with updated schema.")
