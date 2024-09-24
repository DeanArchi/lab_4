import csv
from faker import Faker
import random

fake = Faker('uk_UA')

male = [
    'Олександрович', 'Миколайович', 'Іванович', 'Володимирович', 'Сергійович',
    'Андрійович', 'Богданович', 'Дмитрович', 'Євгенович', 'Кирилович',
    'Павлович', 'Михайлович', 'Юрійович', 'Олегович', 'Семенович',
    'Романович', 'Тарасович', 'Федорович', 'Григорович', 'Вікторович'
]

female = [
    'Олександрівна', 'Миколаївна', 'Іванівна', 'Володимирівна', 'Сергіївна',
    'Андріївна', 'Богданівна', 'Дмитрівна', 'Євгенівна', 'Кирилівна',
    'Павлівна', 'Михайлівна', 'Юріївна', 'Олегівна', 'Семенівна',
    'Романівна', 'Тарасівна', 'Федорівна', 'Григорівна', 'Вікторівна'
]


def generate_employee(gender):
    if gender == 'male':
        first_name = fake.first_name_male()
        middle_name = random.choice(male)
    else:
        first_name = fake.first_name_female()
        middle_name = random.choice(female)

    return {
        'Прізвище': fake.last_name(),
        'Ім’я': first_name,
        'По батькові': middle_name,
        'Стать': 'Чоловіча' if gender == 'male' else 'Жіноча',
        'Дата народження': fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%Y-%m-%d'),
        'Посада': fake.job(),
        'Місто проживання': fake.city(),
        'Адреса проживання': fake.address(),
        'Телефон': fake.phone_number(),
        'Email': fake.email()
    }


employees = []

for _ in range(1200):
    employees.append(generate_employee('male'))
for _ in range(800):
    employees.append(generate_employee('female'))

random.shuffle(employees)

with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(employees)

print("CSV файл створено!")
