import pandas as pd

df = pd.read_csv('data.csv')

disciplines = ['Discipline1', 'Discipline2', 'Discipline3', 'Discipline4', 'Discipline5']

df['Student_Average'] = df[disciplines].mean(axis=1)

print("Таблиця студентів із середнім балом:")
print(df[['Name', 'Surname', 'Student_Average']].to_string())
print('\n')
print("Середній бал групи з кожної дисципліни:")
for discipline in disciplines:
    print(f"{discipline}: {df[discipline].mean()}")