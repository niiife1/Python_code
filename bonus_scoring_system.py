numbers_of_students = int(input())
numbers_of_lectures = int(input())
bonus = int(input())
alll = []
all_lectures = []
for n in range(numbers_of_students):
    attendence_of_students = int(input())
    all_lectures.append(attendence_of_students)
    total_bonus = attendence_of_students / numbers_of_lectures * (5 + bonus)
    alll.append(total_bonus)
    alll.sort()
    all_lectures.sort()
    b = round(alll[-1])
print(f"Max Bonus: {b}.")
print(f"The student has attended {all_lectures[-1]} lectures.")