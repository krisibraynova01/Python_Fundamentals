import re
valid_destination = []
total_length = 0

text = input()
search_pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
valid_destinations = re.finditer(search_pattern, text)

for valid in valid_destinations:
    valid_destination.append(valid[2])
print(f"Destinations: {', '.join(valid_destination)}")

for el in valid_destination:
    total_length += len(el)
print(f"Travel Points: {total_length}")


