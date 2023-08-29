
string = input()
while string != 'End':
    line = input()
    if string == 'SoftUni':
        continue
    for ch in string:
        print(f'{ch}{ch}', end = '')
    print()
