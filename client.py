import socket
import time
import ssl
from encryption import encrypt, decrypt

HOST = input("Enter server IP: ")
PORT = 5000

# 🔐 SSL setup
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = context.wrap_socket(client, server_hostname=HOST)

client.connect((HOST, PORT))

print("Connected to secure server")

username = input("Username: ")
password = input("Password: ")

client.send(encrypt(username).encode())
client.send(encrypt(password).encode())

auth = decrypt(client.recv(1024).decode())

if auth != "AUTH_SUCCESS":
    print("Authentication failed")
    client.close()
    exit()

print("Authentication successful")

while True:
    command = input("Enter command: ")

    if command.lower() == "exit":
        client.send(encrypt("EXIT").encode())
        break

    if command.startswith("ADD_USER"):
        client.send(encrypt(command).encode())
        response = decrypt(client.recv(1024).decode())
        print(response)
        continue

    message = f"CMD|{command}"

    start = time.time()

    client.send(encrypt(message).encode())

    encrypted_response = client.recv(4096).decode()
    output = decrypt(encrypted_response)

    end = time.time()

    print("\nOutput:\n", output)
    print("Execution Time:", end - start, "seconds\n")

client.close()