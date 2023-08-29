single_string = input()
digits = ""
letters = ""
other = ""

for chr in single_string:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        letters += chr
    else:
        other += chr

print(digits)
print(letters)
print(other)