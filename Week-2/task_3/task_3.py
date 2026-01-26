students = ["Vasya", "Petya", "Bobby"]
grades = {}
unique_grades = set()

for name in students:
    g = list(map(int, input(f"{name} (3 grades): ").split()))
    grades[name] = g
    unique_grades.update(g)

print("\nAverage grades:")
for name, g in grades.items():
    print(f"{name}: {sum(g) / len(g):.2f}")

print("\nUnique grades:")
print(unique_grades)
