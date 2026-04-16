# Secure Remote Command Execution System

A Python-based secure remote shell built using a **client-server architecture** with **TCP sockets**, **SSL/TLS encryption**, **SQLite-backed authentication**, **XOR message obfuscation**, and **multi-threaded request handling**.

This project was developed for the **Computer Networks (UE24CS352A)** course at **PES University**.

---

## Team Members

- **Dhanush Rao** â€” PES2UG24CS153
- **Darshan Pawar** â€” PES2UG24CS143
- **Farheen Akhtar** â€” PES2UG24CS164

---

## Overview

This system allows an authenticated client to connect to a remote server, execute shell commands, and receive the output in real time.  
It is designed to demonstrate core networking concepts such as:

- socket programming
- TLS handshake and certificate use
- client-server communication
- multi-threaded server design
- authentication and role-based access control
- audit logging

The project uses only **Python standard library modules** and no external dependencies.

---

## Features

- Secure TCP communication using **SSL/TLS**
- Additional **XOR-based application layer encryption**
- Username/password authentication using **SQLite**
- Persistent command logging with timestamps
- Multi-threaded server for handling multiple clients
- Admin-only **`ADD_USER`** command
- Execution time measurement on the client side
- Simple and portable Python implementation

---

## Project Structure

```text
.
â”œâ”€â”€ client.py
â”œâ”€â”€ server.py
â”œâ”€â”€ encryption.py
â”œâ”€â”€ database_setup.py
â”œâ”€â”€ project.db
â”œâ”€â”€ cert.pem
â”œâ”€â”€ key.pem
â””â”€â”€ README.md
```

### File roles

- **`client.py`** â€” interactive terminal client used to authenticate and send commands
- **`server.py`** â€” secure server that authenticates users, executes commands, and logs activity
- **`encryption.py`** â€” shared XOR encryption/decryption logic
- **`database_setup.py`** â€” initializes the SQLite database and default admin user

---

## System Architecture

The system follows a simple **two-tier client-server design**:

1. The client connects to the server over **TCP**
2. The TCP channel is wrapped inside **SSL/TLS**
3. Every message is additionally encrypted using a shared **XOR cipher**
4. The server authenticates the user from the SQLite database
5. After successful login, the client can send commands
6. The server runs the commands and returns the output
7. All actions are logged in the database

---

## Network Stack

| Layer | Protocol / Mechanism |
|---|---|
| Application | Custom text protocol: `CMD|<command>`, `ADD_USER <user> <pass>`, `EXIT` |
| Presentation | XOR encryption (`KEY = 12`) |
| Session | SSL/TLS |
| Transport | TCP |
| Network | IPv4 |

---

## Database Schema

### `users` table
Stores usernames and XOR-encrypted passwords.

```sql
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
);
```

### `logs` table
Stores command history with timestamps.

```sql
CREATE TABLE IF NOT EXISTS logs (
    username TEXT,
    command  TEXT,
    time     TEXT
);
```

---

## How It Works

### 1) Database setup
Run `database_setup.py` once to create the database and insert the default admin account.

### 2) Server startup
The server opens a TCP socket, loads the TLS certificate, and waits for client connections.  
Each client is handled in a separate thread.

### 3) Client connection
The client connects to the server using SSL/TLS and then sends encrypted credentials.

### 4) Authentication
The server decrypts the credentials, checks them against the database, and returns either:

- `AUTH_SUCCESS`
- `AUTH_FAILED`

### 5) Command execution
After authentication, the client can send commands. The server:

- decrypts the message
- extracts the command
- runs it using `subprocess.getoutput()`
- logs the action
- sends back the result

### 6) Admin-only user management
The `ADD_USER` command is allowed only for the `admin` account.

---

## Installation

### Prerequisites

- Python 3.x
- OpenSSL installed on your system

### Clone the repository

```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

---

## Setup

### 1) Generate SSL certificate files

Create a self-signed certificate for local development/testing:

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 2) Initialize the database

Run:

```bash
python database_setup.py
```

This creates `project.db` and inserts the default admin user.

### 3) Start the server

```bash
python server.py
```

### 4) Run the client

Open another terminal and run:

```bash
python client.py
```

Enter the server IP when prompted.

---

## Default Login

The default admin credentials created by the setup script are:

- **Username:** `admin`
- **Password:** `1234`

> Change this immediately if you plan to reuse the project beyond a demo or lab environment.

---

## Usage

After login, you can enter shell commands such as:

```bash
whoami
date
ls
pwd
```

### Special command

To add a new user as admin:

```bash
ADD_USER alice secret123
```

To exit:

```bash
exit
```

---

## Example Workflow

```text
1. Start server.py
2. Start client.py
3. Enter server IP
4. Login with username and password
5. Send commands
6. Receive output
7. Exit when done
```

---

## Security Notes

This project is meant for **educational use** and demonstrates security concepts, but it is not production-ready.

### Important limitations

- XOR encryption is weak and not cryptographically secure
- The TLS certificate is self-signed
- Client certificate verification is disabled for lab use
- Shell commands are executed directly, so unsafe input can be dangerous
- Passwords are stored using XOR encryption instead of proper hashing

### Recommended improvements

- Replace XOR with **AES-256-GCM**
- Store passwords with **bcrypt** or **Argon2**
- Use a valid CA-signed certificate
- Add command whitelisting
- Add session tokens and timeout handling
- Use stronger input validation

---

## Sample Outputs

### Server
```text
Secure Server started...
Waiting for connections...
```

### Client
```text
Connected to secure server
Authentication successful
```

### Command result
```text
Output:
root
Execution Time: 0.0031 seconds
```

---

## Future Scope

- Replace XOR with strong authenticated encryption
- Use password hashing with salt
- Add proper certificate verification
- Implement a restricted shell
- Add session management
- Support file transfer commands
- Build a web dashboard for logs and user management
- Move to an asyncio-based architecture for scalability
- Add two-factor authentication for admin access

---

## Learning Outcomes

This project demonstrates:

- TCP client-server communication
- SSL/TLS integration in Python
- Secure message handling
- SQLite database integration
- Multi-threaded server programming
- Basic access control and logging
- Practical networking and security implementation

---

## References

- Python Documentation: `socket`, `ssl`, `subprocess`, `sqlite3`
- RFC 5246 â€” Transport Layer Security (TLS) 1.2
- OWASP Password Storage Cheat Sheet
- Standard Computer Networks and Cryptography textbooks

---

## License

This project was created for academic purposes.  
You may adapt it for learning, demonstration, or coursework use.

---

## Author Note

This README is based on the project report and is formatted for GitHub repository use.