factor = int(input())
counter = int(input())
list = []

for num in range(1, counter + 1):
    list.append(num * factor)

print(list)