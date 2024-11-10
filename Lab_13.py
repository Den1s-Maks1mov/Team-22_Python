import csv
import json

# функція запису даних у CSV файл
def write_to_csv(filename, data):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows(data)
        print(f"Дані успішно записано у файл {filename}")
    except FileNotFoundError as e:
        print(f"Помилка запису у файл CSV: {e}")

# функція зчитування даних з CSV файлу та запису їх у JSON файл
def csv_to_json(csv_filename, json_filename):
    try:
        # зитування CSV файл
        with open(csv_filename, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            json_data = [row for row in reader]

        # запис в JSON файл
        with open(json_filename, mode='w', encoding='utf-8') as jsonfile:
            json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)
        print(f"Дані успішно переписано у файл {json_filename}")
    except FileNotFoundError as e:
        print(f"Помилка роботи з файлами: {e}")

# дані для запису в CSV файл (Максимов)
data = [
    ["Name", "Group", "Course", "AADS", "MMOOR", "NM", "OOITB", "PP"],
    ["Максимов Денис Віталійович", "КН-33", "2", "99", "94", "64", "73", "94"]
]

# реалізація функцій (Максимов)
write_to_csv('Lab13_data.csv', data)
csv_to_json('Lab13_data.csv', 'Lab13_data.json')
