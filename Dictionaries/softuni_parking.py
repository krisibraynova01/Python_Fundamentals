n = int(input())
database = {}


for people in range(n):
    command = input().split()
    action = command[0]

    if action == 'register':
        person_name = command[1]
        car_number = command[2]
        if person_name not in database:
            database[person_name] = car_number
            print(f"{person_name} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")

    elif action == 'unregister':
        person_name = command[1]
        if person_name not in database:
            print(f"ERROR: user {person_name} not found")
        else:
            print(f"{person_name} unregistered successfully")
            del(database[person_name])

for user, number in database.items():
    print(f"{user} => {number}")
