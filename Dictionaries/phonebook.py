command = input()
people = {}

while len(command) != 1:
    name, phone_number = command.split("-")
    if name not in people:
        people[name] = phone_number
    else:
        people[name] += phone_number

    command = input()

for searched_name in range(int(command)):
    current_name = input()
    if current_name not in people:
        print(f"Contact {current_name} does not exist.")
    else:
        print(f"{current_name} -> {people[current_name]}")


