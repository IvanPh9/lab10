#Пищик Іван
#Функція відкриття файлу
def openFile(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Не можливо відкрити файл: ", file_name)
        exit(1);
    else:
        print("Файл", file_name, "успішно відкрито")
        return file

#Відкриття файлу
file_t = openFile("Text.txt", "w")

#Запис у файл
if file_t:
    file_t.write("Пищик Іван КН-32/2\n")  # Запис прізвища та групи
    file_t.write("Питання: Яка різниця між списком та кортежем у Python?\n")  # Запис питання
    file_t.close()  # Закриваємо файл після запису