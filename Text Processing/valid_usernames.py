from string import ascii_letters, digits


usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue
    contains_forbidden_char = False
    for letter in username:
        if letter not in allowed_chars:
            contains_forbidden_char = True
            break
    if contains_forbidden_char:
        continue
    print(username)


