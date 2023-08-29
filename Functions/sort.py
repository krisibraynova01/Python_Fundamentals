def sort(num):
    return sorted(num)

integers = [int(x) for x in input().split()]

result = sort(integers)
print(list(result))