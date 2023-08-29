n = int(input())
best_snowball = float('-inf')
output = ''
for _ in range(n):
 weight = int(input())
 need_time = int(input())
 quality = int(input())

 formula = (weight // need_time) ** quality

 if formula > best_snowball:
    best_snowball = formula
    output = f'{weight} : {need_time} = {formula} ({quality})'


print(output)
