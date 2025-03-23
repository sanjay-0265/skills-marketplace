import sqlite3

DB_FILE = "database.sqlite"

def fetch_data():
    """Fetches and displays data from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print("\n📌 USERS TABLE:")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("No users found.")

    print("\n📌 GIGS TABLE:")
    cursor.execute("SELECT * FROM gigs")
    gigs = cursor.fetchall()
    if gigs:
        for gig in gigs:
            print(f"ID: {gig[0]}, Title: {gig[1]}, Description: {gig[2]}, Price: ${gig[3]}, Student ID: {gig[4]}")
    else:
        print("No gigs found.")

    conn.close()

if __name__ == "__main__":
    fetch_data()
