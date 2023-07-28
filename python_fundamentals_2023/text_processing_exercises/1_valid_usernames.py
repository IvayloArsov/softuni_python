import re


def validate_username(username):
    # Check username length
    if len(username) < 3 or len(username) > 16:
        return False

    # Check username format using regular expression
    pattern = r'^[a-zA-Z0-9_-]+$'
    if not re.match(pattern, username):
        return False

    return True


usernames = input().split(", ")

valid_usernames = []
for username in usernames:
    if validate_username(username):
        valid_usernames.append(username)

for valid_username in valid_usernames:
    print(valid_username)
