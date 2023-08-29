sequence = list(map(int, input().split()))

command = input()
collapse = []
while command == 'Finish':
    current_command = input().split()

    if current_command[0] == 'Add':
        value = int(current_command[1])
        sequence.append(value)
    elif current_command[0] == 'Remove':
        value = int(current_command[1])
        if value in sequence:
            sequence.remove(value)
    elif current_command[0] == 'Replace':
        value = int(current_command[1])
        replacement = int(current_command[2])
        for indx, element in enumerate(sequence):
            if element == value:
                sequence[indx] = replacement
                break
    elif current_command[0] == 'Collapse':
        value = int(current_command[1])
        for element in sequence:
            if not element < value:
                collapse.append(element)
        sequence.clear()
        sequence = collapse
    command = input()

print(" ".join(str(x) for x in sequence))








