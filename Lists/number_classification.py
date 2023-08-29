numbers = [x for x in input().split(", ")]
positive = []
negative = []
even = []
odd = []


for number in numbers:
    if int(number) >= 0:
        positive.append(number)
        positive_string = ", ".join(str(number) for number in positive)
    if int(number) < 0:
        negative.append(number)
        negative_string = ", ".join(str(number) for number in negative)
    if number % 2 == 0:
        even.append(number)
        even_string = ", ".join(str(number) for number in even)
    if number % 2 != 0:
        odd.append(number)
        odd_string = ", ".join(str(number) for number in odd)
print(f'Positive: {positive_string}')
print(f'Negative: {negative_string}')
print(f'Even: {even_string}')
print(f'Odd: {odd_string}')

