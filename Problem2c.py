import bcrypt

# Hashing a password
def hash_password(password):
    # Convert the password to bytes and hash it
    salt = bcrypt.gensalt()  # Automatically generates a salt, using default of 12 salt rounds
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt) #Hash the password
    return hashed

# Verifying a password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

#Save hash of password to file
def save_credentials(username, password, role):
    with open('passwd.txt', 'a') as file:
        hashed = hash_password(password) #hash the password
        file.write(f"{username},{hashed.decode('utf-8')},{role}\n") #save to password file

#Check if password is valid
def check_credentials(username, password):
    try:
        with open('passwd.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Only process non-empty lines
                    stored_username, stored_password, role = line.split(',')
                    if username == stored_username and check_password(password, stored_password.encode('utf-8')):
                        return role
    except FileNotFoundError:
        return None
    return None