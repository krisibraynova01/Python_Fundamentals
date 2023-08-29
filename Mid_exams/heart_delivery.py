string = [int(x) for x in input().split("@")]

command = input()
counter = 0
while command != 'Love!':
    current_command = command.split()
    jump = current_command[0]
    length = int(current_command[1])
    counter += length
  




