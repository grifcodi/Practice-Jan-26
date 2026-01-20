import csv

import pandas as pd

df = pd.read_csv('data.csv')

disciplines = ['Discipline1', 'Discipline2', 'Discipline3', 'Discipline4', 'Discipline5']

df['Student_Average'] = df[disciplines].mean(axis=1)

print("Students average:")
print(df[['Name', 'Surname', 'Student_Average']].to_string())
print('\n')
print("Group average:")
for discipline in disciplines:
    print(f"{discipline}: {df[discipline].mean()}")
print('\n')

# with open('data.csv', 'r', newline='') as csvfile:
#     content = csvfile.read()
#     print(content)