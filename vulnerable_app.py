import sqlite3

# Database connection
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

# Vulnerable SQL query
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

cursor.execute(query)
user = cursor.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()
