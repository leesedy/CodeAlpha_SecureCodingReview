# CodeAlpha Task 3 — Secure Coding Review

##  Overview
This repository contains my submission for **Task 3: Secure Coding Review** in the CodeAlpha Cyber Security Internship.

The goal of this task is to:
- Review an insecure Python login script.
- Identify vulnerabilities (hardcoded credentials, plaintext passwords, no hashing, no lockout).
- Rewrite the script into a secure version using best practices:
  - **bcrypt** for password hashing
  - **getpass** for hidden password input
  - **Account lockout mechanism** after multiple failed attempts
- Run **Bandit** (a static analysis tool) to check for potential security issues.
- Document findings in a review report.

---

## ⚡ Requirements
- Python 3.8+
- Dependencies:
  ```bash
  pip install bcrypt bandit

## SETUP INSTRUCTIONS
1. Clone the repository:
   ```bash
    git clone https://github.com/<your-username>/CodeAlpha_SecureCodeReview.git
     cd CodeAlpha_SecureCodeReview
3. Install dependicies:
```bash
    pip install bcrypt bandit
```
## USAGE
Insecure Login (for review)
python login_insecure 
 Username: admin
 Password: 1234

✅ Will log in successfully.
⚠️ Vulnerable because credentials are hardcoded and plaintext. 

## SECURE LOGIN (with fixes)
```bash
python login_secure.py
```
Username: admin
Password: StrongP@ssw0rd
   
✅ Correct password → Login successful!
❌ Wrong password → Access denied! Attempts left: X
🔒 After 5 failures → Account temporarily locked.
   
