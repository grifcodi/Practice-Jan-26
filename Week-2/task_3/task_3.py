students = {
    "Vasya": [],
    "Petya": [],
    "Bobby": [],
}

unique_grades = set()


for name in students:
    print(f"\nGrades for {name}:")
    grades = []
    for i in range(3):
        grade = int(input(f"Grade {i + 1}: "))
        grades.append(grade)
        unique_grades.add(grade)
    students[name] = grades

average_grades = {}

for name, grades in students.items():
    average_grades[name] = sum(grades) / len(grades)


print("\nAverage grades:")
for name, avg in average_grades.items():
    print(f"{name}: {avg:.2f}")

print("\nUnique grades:")
print(unique_grades)