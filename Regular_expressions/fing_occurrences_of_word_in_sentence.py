import re

sentence = input().lower()
search_pattern = input().lower()



result = re.findall(rf'\b{search_pattern}\b', sentence)

print(len(result))