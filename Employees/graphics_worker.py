from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


def calculate_age(birth_date):
    today = datetime.today()
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


try:
    df = pd.read_csv('employees.csv')
    print("Ok, CSV файл відкрито!")
except FileNotFoundError:
    print("Помилка: файл CSV не знайдено!")
    exit()

# Підрахунок статей і виведення результатів у консоль
gender_count = df['Стать'].value_counts()
print("Кількість співробітників за статтю:")
print(gender_count)

# Діаграма для кількості співробітників за статтю (1-а діаграма)
gender_count.plot(kind='bar', color=['#1f77b4', '#ff7f0e'], title='Кількість співробітників за статтю')
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.show()

# Підрахунок вікових категорій
df['Вік'] = df['Дата народження'].apply(calculate_age)
categories = {
    'younger_18': df[df['Вік'] < 18],
    '18-45': df[(df['Вік'] >= 18) & (df['Вік'] <= 45)],
    '45-70': df[(df['Вік'] > 45) & (df['Вік'] <= 70)],
    'older_70': df[df['Вік'] > 70]
}

# Підрахунок співробітників у кожній віковій категорії і виведення в консоль
category_counts = {category: len(data) for category, data in categories.items()}
print("\nКількість співробітників за віковими категоріями:")
for category, count in category_counts.items():
    print(f"{category}: {count} співробітників")

# Побудова загальної діаграми для всіх вікових категорій (2-а діаграма)
pd.Series(category_counts).plot(kind='bar', color=['#ff9999', '#66b3ff', '#ff7f0e', '#2ca02c'], title='Кількість співробітників за віковими категоріями')
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.show()

# Підрахунок співробітників жіночої та чоловічої статі у кожній віковій категорії
print("\nКількість співробітників за статтю у кожній віковій категорії:")
gender_by_category_combined = pd.DataFrame()

for category, data in categories.items():
    gender_by_category = data['Стать'].value_counts()
    gender_by_category_combined[category] = gender_by_category

    print(f"\nКатегорія {category}:")
    print(gender_by_category)

# Побудова стовпчастої діаграми для статі у кожній віковій категорії (3-я діаграма)
gender_by_category_combined.plot(kind='bar', title='Стать у кожній віковій категорії', color=['#1f77b4', '#ff7f0e', '#ff9999', '#2ca02c'])
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.show()
