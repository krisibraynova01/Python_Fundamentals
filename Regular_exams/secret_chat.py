concealed_message = input()
command = input()

while command != 'Reveal':
    command_args = command.split(":|:")
    if "InsertSpace" in command_args:
        index = int(command_args[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    if "Reverse" in command_args:
        substring = command_args[1]
        if substring in concealed_message:
           reverse_substring = substring[::-1]
           concealed_message = concealed_message.replace(substring, reverse_substring,1)
           print(concealed_message)
        else:
            print("error")
    if "ChangeAll" in command_args:
        substring = command_args[1]
        replacement = command_args[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()
print(f"You have a new text message: {concealed_message}")


