age = int(input())

if age <= 14:
    print('drink toddy')
elif age > 14 and age <= 18:
    print('drink coke')
elif age > 19 and age <= 21:
    print('drink beer')
else:
    print('drink whisky')