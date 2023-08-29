list = input().split('!')

command = input()

while command != 'Go Shopping!':
    current_command = command.split()
    action = current_command[0]
    item = current_command[1]

    if action == 'Urgent' and item not in list:
        list.insert(0, item)
    elif action == 'Unnecessary' and item in list:
        list.remove(item)
    elif action == 'Correct' and item in list:
        newItem = current_command[2]
        current_index = list.index(item)
        list[current_index] = newItem

    elif action == 'Rearrange' and item in list:
        list.remove(item)
        list.append(item)


    command = input()

print(', '.join(list))









