import pandas as pd
from datetime import datetime


def calculate_age(birth_date):
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


try:
    df = pd.read_csv('employees.csv')
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено!")
    exit()

df['Вік'] = df['Дата народження'].apply(calculate_age)

categories = {
    'younger_18': df[df['Вік'] < 18],
    '18-45': df[(df['Вік'] >= 18) & (df['Вік'] <= 45)],
    '45-70': df[(df['Вік'] > 45) & (df['Вік'] <= 70)],
    'older_70': df[df['Вік'] > 70]
}

with pd.ExcelWriter('employees.xlsx') as writer:
    df.to_excel(writer, sheet_name='all', index=False)

    for category, data in categories.items():
        data = data.copy()
        data['№'] = range(1, len(data) + 1)
        data.to_excel(writer, sheet_name=category, index=False,
                      columns=['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])


print("Ok, XLSX файл створено!")
