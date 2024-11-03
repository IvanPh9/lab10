#Пищик Іван
#Функція відкриття файлу
def openFile(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
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
    # Очищуємо файл, щоб не дублювати у файлі текст написаний попередніми студентами
    file_t.truncate()

    # Пищик Іван
    file_t.write("Пищик Іван КН-32/2\n")  # Запис прізвища та групи
    file_t.write("Питання: Яка різниця між списком та кортежем у Python?\n")  # Запис питання
    # Дяченко Юлія
    file_t.write("\nДяченко Юлія КН-31/2\n"
                 "Список можна редагувати - це стосується як розміру списку, так і самих елементів у ньому.\n"
                 "А кортеж змінювати не можна.\n"
                 "Питання: В чому різниця між арифметичними операторами '/' та '// у Python'?\n")  # Запис питання
    # Івженко Тимофій
    file_t.write("\nІвженко Тимофій КН-31/2\n"
                 "Оператор / в Python виконує звичайне ділення з поверненням результату з дробовою частиною (float),\n"
                 "а // — це оператор цілочислового ділення, який повертає лише цілу частину результату, відкидаючи дробову.\n"
                 "Питання: Чим відрізняються операції ** та ^ у Python?\n")
    # Рожченко Іван
    file_t.write("\nРожченко Іван КН-31/2\n"
                 "Оператор ** в Python використовується для піднесення числа до степеня,\n"
                 "а ^ виконує побітове порівняння двох чисел і якщо лише один з двох дорівнює 1, то ставить 1, а якщо 0 і 0 або 1 і 1, то 0.\n"
                 "Питання: Чим відрізняються режими відкриття файлів 'a' та 'w' у Python?\n")
    # Руденко Дарина
    file_t.write("\nРуденко Дарина КН-31/2\n")
    file_t.write("Режим 'w' перезаписує файл, якщо він існує, тоді як режим 'a' додає дані в кінець файлу без видалення вже наявного вмісту. ")
    file_t.close()  # Закриваємо файл після запису
    print("Файл закрито.")  # Повідомлення про закриття файлу