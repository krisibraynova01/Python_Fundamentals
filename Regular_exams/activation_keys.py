sequence_of_chars = input()
command = input()

while command != "Generate":
    command_args = command.split(">>>")
    if "Contains" in command:
        substring = command_args[1]
        if substring in sequence_of_chars:
            print(f"{sequence_of_chars} contains {substring}")
        else:
            print("Substring not found!")
    if "Flip" in command:
        upper_or_lower = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        if "Upper" in upper_or_lower:
            sequence_of_chars = sequence_of_chars[:start_index].lower()+sequence_of_chars[start_index:end_index].upper()+sequence_of_chars[end_index:].lower()
            print(sequence_of_chars)
        if "Lower" in upper_or_lower:
            sequence_of_chars = sequence_of_chars[:start_index] + sequence_of_chars[start_index:end_index].lower() + sequence_of_chars[end_index:]
            print(sequence_of_chars)
    if 'Slice' in command:
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        sequence_of_chars = sequence_of_chars[:start_index]+sequence_of_chars[end_index:]
        print(sequence_of_chars)

    command = input()

print(f"Your activation key is: {sequence_of_chars}")



