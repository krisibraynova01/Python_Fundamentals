sequence = list(map(int, input().split(' ')))
command = input()
collapse = []
while not command == 'Finish':
    current_command = command.split()
    if current_command[0] == 'Add':
        add_value = int(current_command[1])
        sequence.append(add_value)

    elif current_command[0] == 'Remove':
        remove_value = int(current_command[1])
        if remove_value in sequence:
            sequence.remove(remove_value)

    elif current_command[0] == 'Replace':
        value = int(current_command[1])
        replace = int(current_command[2])
        for index, el in enumerate(sequence):
            if el == value:
                sequence[index] = replace
                break

    elif current_command[0] == 'Collapse':
        collapse_value = int(current_command[1])
        for el in sequence:
            if not el < collapse_value:
                collapse.append(el)
        sequence.clear()
        sequence = collapse

    command = input()

print(*sequence, sep=" ")