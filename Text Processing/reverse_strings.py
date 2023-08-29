command = input()


while command != 'end':
    reversed_text = ""
    for ch in reversed(command):
        reversed_text += ch
    print(command + " = " + reversed_text)

    command = input()

