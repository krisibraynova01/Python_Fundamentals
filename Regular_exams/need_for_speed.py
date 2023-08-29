num_of_cars = int(input())
cars = {}

for _ in range(num_of_cars):
    cars_args = input().split("|")
    car = cars_args[0]
    mileage = int(cars_args[1])
    fuel_available = int(cars_args[2])
    cars[car] = {'mileage': mileage, 'fuel': fuel_available}

while True:
    line = input()

    if line == 'Stop':
        break
    command = line.split(" : ")
    if 'Drive' in command:
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]['mileage'] >= 100000:
            del cars[car]
            print(f'Time to sell the {car}!')
    elif 'Refuel' in command:
        car = command[1]
        fuel = int(command[2])
        liters = 0
        if cars[car]['fuel'] + fuel > 75:
            print(f"{car} refueled with {75-cars[car]['fuel']} liters")
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel
            liters = fuel
            print(f"{car} refueled with {liters} liters")
    elif 'Revert' in command:
        car = command[1]
        kilometers = int(command[2])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        else:
            print(f'{car} mileage decreased by {kilometers} kilometers')
for key, value in cars.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")











