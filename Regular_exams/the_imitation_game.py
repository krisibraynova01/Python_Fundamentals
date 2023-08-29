message = input()

command = input()

while command != 'Decode':
    command_args = command.split('|')
    if 'Move' in command_args:
        num_of_letters = int(command_args[1])
        message = message[num_of_letters:] + message[:num_of_letters]
    elif 'Insert' in command_args:
        index = int(command_args[1])
        value = command_args[2]
        message = message[:index] + value + message[index:]
    elif 'ChangeAll' in command_args:
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
