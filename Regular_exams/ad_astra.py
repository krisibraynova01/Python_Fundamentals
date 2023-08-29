import re

text = input()
total_calories = 0


search_pattern = r'(#|\|)([A-Za-z\s]+)\1(\d\d\/\d\d\/\d\d)\1(\d+)\1'
valid_patterns = re.finditer(search_pattern, text)

for valid1 in valid_patterns:
    total_calories += int(valid1[4])
print(f"You have food to last you for: {total_calories // 2000} days!")

valid_patterns = re.finditer(search_pattern, text)
for valid in valid_patterns:
    calories = int(valid[4])
    item_name = valid[2]
    expiration_date = valid[3]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")




