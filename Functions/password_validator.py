def check_pass(str):
    counter_digit = 0
    is_valid = True
    if not 6 <= len(str) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not str.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for digit in str:
        if digit.isdigit():
            counter_digit += 1
    if counter_digit < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print('Password is valid')
    return

password = input()
check_pass(password)
