divisor = int(input())
boundary = int(input())

result = 0
for num in range(1, boundary+1):
    if num % divisor == 0:
        result = num

print(result)
