def check_password_validity(password):
    if len(password) < 6 or len(password) > 10:
        print("Password must be between 6 and 10 characters")

    elif not password.isalnum():
        print("Password must consist only of letters and digits")

    elif sum(1 for char in password if char.isdigit()) < 2:
        print("Password must have at least 2 digits")

    # Password is valid if all rules are fulfilled
    else:
        print("Password is valid")


password = input()
check_password_validity(password)
