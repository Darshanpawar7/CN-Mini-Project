# 🔐 Secure Remote Command Execution System

A Python-based secure remote shell built using a **client-server architecture** with **TCP sockets**, **SSL/TLS encryption**, **SQLite authentication**, and **multi-threaded execution**.

---

## 📌 Project Information

| Field         | Details                        |
| ------------- | ------------------------------ |
| Course        | Computer Networks (UE24CS352A) |
| University    | PES University                 |
| Academic Year | 2024 – 2025                    |
| Project Type  | Mini Project                   |
| Language Used | Python                         |

---

## 👨‍💻 Team Members

| Name           | USN           |
| -------------- | ------------- |
| Dhanush Rao    | PES2UG24CS153 |
| Darshan Pawar  | PES2UG24CS143 |
| Farheen Akhtar | PES2UG24CS164 |

---

## 📖 Overview

This project allows a client to securely connect to a remote server and execute system-level commands. The output is returned in real time.

It demonstrates key networking concepts like:

* Client-server communication
* TCP socket programming
* TLS encryption
* Authentication systems
* Multi-threading
* Logging and auditing

---

## ✨ Features

* 🔒 SSL/TLS encrypted communication
* 🔐 Additional XOR-based message encryption
* 👤 User authentication using SQLite
* 📜 Command logging with timestamps
* ⚡ Multi-threaded server (handles multiple clients)
* 🛡️ Admin-only user creation
* ⏱️ Command execution time tracking

---

## 🏗️ Project Structure

```bash
.
├── client.py              # Client terminal
├── server.py              # Secure server
├── encryption.py          # XOR encryption logic
├── database_setup.py      # Database initialization
├── project.db             # SQLite database
├── cert.pem               # SSL certificate
├── key.pem                # SSL key
└── README.md
```

---

## 🧠 System Architecture

| Component      | Technology Used  | Purpose              |
| -------------- | ---------------- | -------------------- |
| Client         | Python + SSL     | Sends commands       |
| Server         | Python + Threads | Executes commands    |
| Encryption     | XOR Cipher       | Message obfuscation  |
| Security Layer | SSL/TLS          | Secure communication |
| Database       | SQLite           | Stores users & logs  |

---

## 🌐 Network Stack

| Layer        | Implementation                              |
| ------------ | ------------------------------------------- |
| Application  | Custom Protocol (`CMD`, `ADD_USER`, `EXIT`) |
| Presentation | XOR Encryption                              |
| Session      | SSL/TLS                                     |
| Transport    | TCP                                         |
| Network      | IPv4                                        |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd <your-folder>
```

### 2️⃣ Generate SSL Certificate

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 3️⃣ Initialize Database

```bash
python database_setup.py
```

### 4️⃣ Start Server

```bash
python server.py
```

### 5️⃣ Run Client

```bash
python client.py
```

---

## 🔑 Default Credentials

| Username | Password |
| -------- | -------- |
| admin    | 1234     |

---

## 💻 Usage

### Run Commands

```
whoami
date
ls
pwd
```

### Add New User (Admin Only)

```
ADD_USER username password
```

### Exit

```
exit
```

---

## 📊 Sample Output

```
Output:
root

Execution Time: 0.0031 seconds
```

---

## ⚠️ Limitations

* XOR encryption is weak (not secure for real-world use)
* Self-signed SSL certificate
* No password hashing
* Executes raw shell commands (security risk)
* Fixed buffer size for communication

---

## 🚀 Future Improvements

* Replace XOR with AES encryption
* Use bcrypt/Argon2 for password hashing
* Add command restrictions
* Implement session tokens
* Build web dashboard
* Add file transfer support

---

## 🎯 Learning Outcomes

* TCP & Socket Programming
* SSL/TLS Implementation
* Client-Server Architecture
* Multi-threading
* Database Integration
* Security Concepts

---

## 📚 References

* Python Documentation (socket, ssl, sqlite3)
* RFC 5246 (TLS 1.2)
* OWASP Password Storage Guidelines
* Computer Networks Textbooks

---

## 📌 Note

This project is built for **educational purposes** and demonstrates networking and security fundamentals.
