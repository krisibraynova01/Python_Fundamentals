emp1_per_hour = int(input())
emp2_per_hour = int(input())
emp3_per_hour = int(input())
hours_counter = 0
student_counter = int(input())
sum_of_employees_per_hour = emp1_per_hour + emp2_per_hour + emp3_per_hour

while student_counter > 0:
    if hours_counter % 4 == 0:
        hours_counter += 1
    student_counter -= sum_of_employees_per_hour
    if student_counter <= 0:
        break
    hours_counter += 1

print(f'Time needed: {hours_counter}h.')





