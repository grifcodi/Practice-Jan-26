class Student:
    def __init__(self, name, group, avg_grade):
        self.name = name
        self.group = group
        self.avg_grade = avg_grade

    def show_info(self):
        print(f"Name: {self.name}, Group: {self.group}, Average Grade: {self.avg_grade}")

stud_list = [
    Student("Vasya", "IPZ-31", 7),
    Student("Petya", "IPZ-30", 99),
    Student("Bobby", "IPZ-3-1", 99.9),
]

for s in stud_list:
    s.show_info()