from math import ceil
num_of_students = int(input())
num_of_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
best_student = 0
max_attendance = 0

for attendance in range(1, num_of_students + 1):
    attendances = int(input())
    total_bonus = (attendances / num_of_lectures) * (5 + additional_bonus)
    if total_bonus > best_student:
        best_student = total_bonus
        max_attendance = attendances
    elif total_bonus < best_student:
        number_to_round = total_bonus

print(f'Max Bonus: {ceil(best_student)}.')
print(f'The student has attended {max_attendance} lectures.')



