string = input()

command = input()

while command != 'Done':
    command_args = command.split()
    if "TakeOdd" in command_args:
        string = string[1::2]
        print(string)
    if "Cut" in command_args:
        index = int(command_args[1])
        length = int(command_args[2])
        string = string[:index]+string[length+index:]
        print(string)
    if "Substitute" in command_args:
        substring = command_args[1]
        substitute = command_args[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {string}")
