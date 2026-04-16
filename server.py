import socket
import subprocess
import time
import threading
import sqlite3
import ssl
from encryption import encrypt, decrypt

HOST = "0.0.0.0"
PORT = 5000


def authenticate(username, password):
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()

    encrypted_password = encrypt(password)

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, encrypted_password))
    result = cursor.fetchone()

    conn.close()
    return result is not None


def log_event(username, command):
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO logs VALUES (?, ?, ?)", (username, command, timestamp))

    conn.commit()
    conn.close()


def add_user(new_user, new_pass):
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()

    encrypted_password = encrypt(new_pass)

    cursor.execute("INSERT INTO users VALUES (?, ?)", (new_user, encrypted_password))

    conn.commit()
    conn.close()


def handle_client(conn, addr):
    print("Connected by", addr)

    try:
        username = decrypt(conn.recv(1024).decode())
        password = decrypt(conn.recv(1024).decode())

        if authenticate(username, password):
            conn.send(encrypt("AUTH_SUCCESS").encode())
            print("User authenticated:", username)
        else:
            conn.send(encrypt("AUTH_FAILED").encode())
            conn.close()
            return

        while True:
            message = decrypt(conn.recv(1024).decode())

            if message == "EXIT":
                log_event(username, "DISCONNECTED")
                break

            if message.startswith("ADD_USER"):
                if username != "admin":
                    conn.send(encrypt("Access Denied: Only admin can add users").encode())
                    continue

                try:
                    _, new_user, new_pass = message.split()
                    add_user(new_user, new_pass)
                    conn.send(encrypt("User added successfully").encode())
                except:
                    conn.send(encrypt("Error adding user").encode())
                continue

            parts = message.split("|")

            if parts[0] == "CMD":
                command = parts[1]

                log_event(username, command)

                output = subprocess.getoutput(command)

                conn.send(encrypt(output).encode())

    except:
        print("Error with client:", addr)

    finally:
        conn.close()


# 🔐 SSL SETUP
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Secure Server started...")
print("Waiting for connections...")

while True:
    conn, addr = server.accept()

    # 🔐 Wrap connection with SSL
    secure_conn = context.wrap_socket(conn, server_side=True)

    thread = threading.Thread(target=handle_client, args=(secure_conn, addr))
    thread.start()