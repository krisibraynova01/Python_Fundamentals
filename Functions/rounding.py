def rounding_nums(num):
    rounded_nums = []
    for number in num:
        rounded_number = round(number)
        rounded_nums.append(rounded_number)
        return rounded_nums




numbers = [float(nums) for nums in input().split()]

print(rounding_nums(numbers))
