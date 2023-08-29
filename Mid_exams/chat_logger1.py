line = list(input().split(' '))
chat = []

while line[0] != 'end':
    command = line[0]
    if command == 'Chat':
        message = line[1]
        chat.append(message)

    if command == 'Delete':
        message = line[1]
        if message in chat:
            chat.remove(message)

    if command == 'Edit':
        message = line[1]
        edited_message = line[2]
        for i in range(len(chat)):
            if chat[i] == message:
                chat[i] = edited_message

    if command == 'Pin':
        message = line[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)

    if command == 'Spam':
        for num in range(1, len(line)):
            message = line[num]
            chat.append(message)

    line = list(input().split(' '))

print('\n'.join(chat))