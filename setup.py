import sqlite3
import os

DB_FILE = "database.sqlite"

def init_db():
    """Creates the database and inserts sample data if not present."""
    db_exists = os.path.exists(DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            email TEXT UNIQUE, 
            password TEXT
        )
    """)

    # Create Gigs Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gigs (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT, 
            description TEXT, 
            price REAL, 
            student_id INTEGER
        )
    """)

    # Insert Sample Users if Empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO users (name, email, password) VALUES (?, ?, ?)
        """, [
            ("John Doe", "john@example.com", "password123"),
            ("Jane Smith", "jane@example.com", "securepass"),
            ("Alice Brown", "alice@example.com", "mypassword"),
            ("Aishya", "ashiya@example.com", "mypassword123")
        ])
        print("✅ Sample users added.")

    # Insert Sample Gigs if Empty
    cursor.execute("SELECT COUNT(*) FROM gigs")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
            INSERT INTO gigs (title, description, price, student_id) VALUES (?, ?, ?, ?)
        """, [
            ("Web Development", "Build a website for a startup", 100.0, 1),
            ("Graphic Design", "Create a logo for a company", 50.0, 2),
            ("Tutoring", "Teach Python to beginners", 30.0, 3),
            ("Full Stack Development", "Build a website for a startup", 120.0, 4)
        ])
        print("✅ Sample gigs added.")

    conn.commit()
    conn.close()

    if not db_exists:
        print("✅ Database setup complete.")
    else:
        print("✅ Database already exists. No new tables created.")

if __name__ == "__main__":
    init_db()
