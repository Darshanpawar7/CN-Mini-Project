Project: Secure Remote Command Execution System

Description:
A secure client-server system where authenticated users can execute commands remotely.

Features:
- Multi-client support
- Authentication using SQLite database
- XOR-based encryption
- Command execution on server
- Logging of user activity
- Dynamic user creation (ADD_USER)

How to Run:

1. Setup database:
   python database_setup.py

2. Start server:
   python server.py

3. Run client:
   python client.py

Login:
Username: admin
Password: 1234

Commands:
- whoami
- dir
- date
- ADD_USER <username> <password>
- exit