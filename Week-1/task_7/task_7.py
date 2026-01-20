students = [
    {
        "Name": "Name1",
        "Surname": "Surname1",
        "Grades": [90, 85, 30, 25, 100]
    },
    {
        "Name": "Name2",
        "Surname": "Surname2",
        "Grades": [45, 0, 90, 10, 95]
    },
    {
        "Name": "Name3",
        "Surname": "Surname3",
        "Grades": [41, 33, 87, 54, 98]
    },
    {
        "Name": "Name4",
        "Surname": "Surname4",
        "Grades": [68, 91, 18, 63, 97]
    }
]

def print_table(table):
    print("Name\tSurname\tAv. Grade")
    print("-" * 35)
    for student in table:
        avg_grade = 0
        for grade in student["Grades"]:
            avg_grade += grade
        avg_grade /= len(student["Grades"])
        print(student["Name"] + "\t" + student["Surname"] + "\t" + str(avg_grade))

    print("-" * 35)

def discipline_avg(table, i):
    avg = 0
    for student in table:
        avg += student["Grades"][i]
    avg /= len(table)
    return avg

def group_average(table):
    print("-" * 35)
    for i in range(len(table[0]["Grades"])):
        print(f"Discipline {i+1}: {discipline_avg(table, i)}")
    print("-" * 35)


print_table(students)
print('\n')
group_average(students)
