from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect("database.sqlite")
    conn.row_factory = sqlite3.Row
    return conn

# Route for login authentication
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (data["email"], data["password"]))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({"success": True})
    return jsonify({"success": False})

# Route to fetch all gigs
@app.route("/gigs", methods=["GET"])
def get_gigs():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gigs")
    gigs = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in gigs])

# Serve HTML pages
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gigs.html")
def gigs():
    return render_template("gigs.html")

if __name__ == "__main__":
    app.run(debug=True)
