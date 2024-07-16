import re

def password_strength(password):
    strength = 0
    feedback = ""

    if len(password) < 8:
        feedback += "Password is too short. It should be at least 8 characters long.\n"
    else:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one uppercase letter.\n"

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one lowercase letter.\n"

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback += "Password should contain at least one number.\n"

    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one special character.\n"

    if strength < 3:
        feedback += "Password is weak. It should contain a mix of characters, numbers, and special characters.\n"
    elif strength == 3:
        feedback += "Password is medium strength. It's a good start, but consider adding more complexity.\n"
    else:
        feedback += "Password is strong! It meets all the criteria for a secure password.\n"

    return feedback

password = input("Enter a password: ")
print(password_strength(password))
