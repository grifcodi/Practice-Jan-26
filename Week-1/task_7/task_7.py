class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


group = [
    Student("Name1", "Surname1",  [90, 85, 30, 25, 100]),
    Student("Name2", "Surname2", [45, 0, 90, 10, 95]),
    Student("Name3", "Surname3", [41, 33, 87, 54, 98]),
    Student("Name4", "Surname4", [68, 91, 18, 63, 97]),
]

def print_table(table):
    print("Name\tSurname\tAv. Grade")
    print("-" * 35)
    for row in table:
        print(row.name, row.surname, row.average())
    print("-" * 35)

def discipline_avg(table, i):
    avg = 0
    for row in table:
        avg += row.grades[i]
    avg /= len(table)
    return avg

def group_average(table):
    print("-" * 35)
    print("Discipline 1 avg.: ", discipline_avg(table, 0))
    print("Discipline 2 avg.: ", discipline_avg(table, 1))
    print("Discipline 3 avg.: ", discipline_avg(table, 2))
    print("Discipline 4 avg.: ", discipline_avg(table, 3))
    print("Discipline 5 avg.: ", discipline_avg(table, 4))
    print("-" * 35)


print_table(group)
print('\n')
group_average(group)