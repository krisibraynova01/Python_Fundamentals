def swap(indx1, indx2, list):
    list[indx1], list[indx2] = list[indx2], list[indx1]

def multiply(indx1, indx2, list):
    product = list[indx1] * list[indx2]
    list[indx1] = product

def decrease(list):
    for element in range(len(list)):
        numbers[element] -= 1

numbers = [int(num) for num in input().split()]

command = input()

while command != 'end':
    current_command = command.split()
    action = current_command[0]

    if action == 'swap':
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        swap(index1, index2, numbers)
    elif action == 'multiply':
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        multiply(index1, index2, numbers)
    elif action == 'decrease':
        decrease(numbers)
    command = input()

print(', '.join([str(x) for x in numbers]))






