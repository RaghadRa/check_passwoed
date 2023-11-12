def check_password(password):
    # Check password length
    if len(password) < 12 or len(password) > 25:
        return False
    
    # Check for lowercase letters
    if not any(c.islower() for c in password):
        return False
    
    # Check for uppercase letters
    if not any(c.isupper() for c in password):
        return False
    
    # Check for numbers
    if not any(c.isdigit() for c in password):
        return False
    
    # Check for suffix
    if not password.endswith("@gmail.com"):
        return False
    
    # All criteria met
    return True

# Get passwords from user input
passwords = input("Enter comma separated passwords: ")

# Split passwords by comma
passwords = passwords.split(",")

# Check each password and print valid ones
for password in passwords:
    password = password.strip() # remove leading/trailing whitespace
    if check_password(password):
        print(password)
