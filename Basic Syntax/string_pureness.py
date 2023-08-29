n = int(input())

for i in range(n):
    string = input()

    is_pure = True

    for ch in string:
        if ch == '.' or ch == ',' or ch == '_':
            is_pure = False

    if is_pure == True:
        print(f'{string} is pure.')

    else:
        print(f'{string} is not pure!')
