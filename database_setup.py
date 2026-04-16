import sqlite3
from encryption import encrypt

conn = sqlite3.connect("project.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    username TEXT,
    command TEXT,
    time TEXT
)
""")

# Insert default user (encrypted password)
cursor.execute("SELECT * FROM users WHERE username=?", ("admin",))
if cursor.fetchone() is None:
    encrypted_password = encrypt("1234")
    cursor.execute("INSERT INTO users VALUES (?, ?)", ("admin", encrypted_password))

conn.commit()
conn.close()

print("Database ready with encrypted passwords")