# відкриття файлу і його перевірка на те, що він відкрився
def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print(f"Файл {file_name} не відкрився!")
        return None
    else:
        print(f"Файл {file_name} відкрився!")
        return file

file1_name = "Laboratory10_text.txt"

# створення і запис питання у файл Laboratory10_text.txt (Максимов)
file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    file_1_w.write("     ----===== ФАЙЛ ДЛЯ КОРПОРАТИВНИХ ПИТАНЬ =====----     \n")
    file_1_w.write("-----------------------------------------------------------\n")
    file_1_w.write("Максимов Денис:\n")
    file_1_w.write("Яким чином можна реалізувати зчитування даних з файлу?\n")
    file_1_w.write("Якщо точніше, то які функції варто використовувати для зчитування контенту текстового файлу для пдальшої взаємодії?\n")    
    print("Текст Максимова Дениса було додано до файлу Laboratory10_text.txt!")
    file_1_w.close()
    print("Файл Laboratory10_text.txt закрився!")
