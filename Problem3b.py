import re

#Check that username is unique from existing usernames
def validate_username(username):
    try:
        with open('passwd.txt', 'r') as file:
            for line in file:
                stored_username = line.strip().split(',')[0]
                if username == stored_username:
                    return "Username already exists"
        return None
    except FileNotFoundError:
        return None

#Define the proactive password checker policy
def validate_password(username, password):
    #password is not the same as username (case insensitive)
    if password.lower() == username.lower(): 
        return "Password cannot be the same as the username."
    #common passwords source: https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords
    with open('common_passwords.txt', 'r') as file: 
        common_passwords = file.read().splitlines()
        if password in common_passwords:
            return "Password is a common password and is not allowed."
    #regex for other password strength requirements
    if not re.search(r'[A-Z]', password):
        return "Must include at least 1 uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Must include at least 1 lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Must include at least 1 digit."
    if not re.search(r'[!@#$%*&]', password):
        return "Must include at least 1 special character (!@#$%*&)."
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    return None  # all checks pass