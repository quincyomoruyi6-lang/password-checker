# password_checker.py

import re


def check_password_strength(password):
    # Check length
    if len(password) < 6:
        return "Weak", "Password too short"

    # Check for letters, numbers, and special characters
    if (re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):
        return "Strong", "Good job! Your password is strong."

    # Medium strength: letters + numbers
    if (re.search(r"[A-Za-z]", password) and re.search(r"[0-9]", password)):
        return "Medium", "Your password could be stronger. Add special characters and uppercase letters."

    # Otherwise weak
    return "Weak", "Your password is weak. Use letters, numbers, and special characters."


# Main program
print("=== Password Strength Checker ===")
user_password = input("Enter a password to check: ")

strength, message = check_password_strength(user_password)

print(f"Strength: {strength}")
print(f"Message: {message}")
