command = list(input().split(' '))
chat_line = []


while command[0] != 'end':
    action = command[0]

    if action == 'Chat':
        msg = command[1]
        chat_line.append(msg)
    if action == 'Delete':
        msg = command[1]
        if msg in chat_line:
         chat_line.remove(msg)
    if action == 'Edit':
        msg = command[1]
        edit_version = command[2]

        for element in range(len(chat_line)):
            if chat_line[element] == msg:
                chat_line[element] = edit_version

    if action == 'Pin':
        msg = command[1]
        if msg in chat_line:
         chat_line.remove(msg)
         chat_line.append(msg)
    if action == 'Spam':
        for element in range(1, len(command)):
            msg = command[element]
            chat_line.append(msg)

    command = list(input().split(' '))


print('\n'.join(chat_line))

