import csv
import json
import os


print("Выполняется Задание 1")

if not os.path.exists('country.json'):
    country_data = {
        "страна": "Франция",
        "столица": "Париж",
        "население": 67000000
    }
    with open('country.json', 'w', encoding='utf-8') as file:
        json.dump(country_data, file, ensure_ascii=False, indent=2)

with open('country.json', 'r', encoding='utf-8') as file:
    country_data = json.load(file)

country_data['язык'] = "французский"

with open('country.json', 'w', encoding='utf-8') as file:
    json.dump(country_data, file, ensure_ascii=False, indent=2)

print("Задание 1 выполнено: country.json обновлен")


print("Выполняется Задание 2")

if not os.path.exists('test_json.json'):
    test_data_json = {
        "Имя": "Анна",
        "Возраст": 56,
        "Город": "Москва"
    }
    with open('test_json.json', 'w', encoding='utf-8') as file:
        json.dump(test_data_json, file, ensure_ascii=False, indent=2)

with open('test_json.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

new_employee = {
    'Имя': data['Имя'],
    'Возраст': str(data['Возраст']),
    'Город': data['Город'],
    'Должность': 'Стажёр',
    'Зарплата': '50000'
}

csv_filename = 'employees_with_salary.csv'
fieldnames_csv = ['Имя', 'Возраст', 'Город', 'Должность', 'Зарплата']

file_exists = os.path.isfile(csv_filename)

if file_exists:
    with open(csv_filename, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_csv)
        writer.writerow(new_employee)
else:
    with open(csv_filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames_csv)
        writer.writeheader()
        writer.writerow(new_employee)

print("Задание 2 выполнено: данные добавлены в employees_with_salary.csv")
print("Все задания выполнены!")