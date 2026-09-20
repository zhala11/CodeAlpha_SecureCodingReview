import sqlite3
import hashlib
import getpass

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")
password = getpass.getpass("Password: ")

password_hash = hashlib.sha256(password.encode()).hexdigest()

query = "SELECT * FROM users WHERE username = ? AND password_hash = ?"

cursor.execute(query, (username, password_hash))
user = cursor.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid username or password.")

conn.close()
