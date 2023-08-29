n = int(input())
students = {}
count = 0

for student in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)


for student_name, grd in students.items():
    average_grade = sum(grd) / len(grd)
    if average_grade >= 4.50:
        print(f"{student_name} -> {average_grade:.2f}")



