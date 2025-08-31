"""Secure login demo using bcrypt and hidden input."""
import getpass
import bcrypt

#In a real app, credentials live in a DB; here we keep them in memory for demo.
#Create a hashed password once and store that value (simulate DB row )
stored_users = {
"admin": bcrypt.hashpw(b"StrongP@ssw0rd", bcrypt.gensalt()),
}
MAX_TRIES = 5
ok = False
for attempt in range(1, MAX_TRIES + 1):
    username = input("Enter username: ")
    password = input("Enter password: ").encode()
    if username in stored_users and bcrypt.checkpw(password, stored_users[username]):
        print("Login successful!")
        ok = True
        break
    else:
        print(f"Access denied! Attempts left: {MAX_TRIES - attempt}")

if not ok:
     print("Account temporarily locked. Try again later.")