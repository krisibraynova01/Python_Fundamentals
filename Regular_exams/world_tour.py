def is_valid_index(index, seq):
    return 0 <= index < len(seq)


stops = input()

while stops != "Travel":
    command_args = input().split(":")
    command = command_args[0]

    if command == 'Add Stop':
        index = int(command_args[1])
        new_stop = command_args[2]
        if is_valid_index(index, stops):
            stops = stops[:index] + new_stop + stops[index:]
        print(stops)
    elif command == 'Remove Stop':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if is_valid_index(start_index, stops) and is_valid_index(end_index, stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif command == 'Switch':
        old_string = command_args[1]
        new_string = command_args[2]
        stops = stops.replace(old_string, new_string)

        print(stops)
        command_args = input()

print(f'Ready for world tour! Planned stops: {stops}')
