journal = input().split(", ")

command = input()

while command != 'Craft!':
    current_command = command.split("-")
    action = current_command[0]
    item = current_command[1]

    if action == 'Collect' and item not in journal:
        journal.append(item)
    elif action == 'Drop' and item in journal:
        journal.remove(item)
    elif action == 'Combine Items':
        item.split(':')
        oldItem = item[0]
        if oldItem in journal:
         newItem = item[1]
         current_index = journal.index(oldItem)
         journal.insert(current_index + 1, newItem)
    elif action == 'Renew' and item in journal:
        journal.remove(item)
        journal.append(item)

    command = input()

print(', '.join(journal))

