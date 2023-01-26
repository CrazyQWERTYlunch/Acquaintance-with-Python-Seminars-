from export_import_data import *
from print_data import print_data
from search_data import search_data

def greeting():
    print("Этой ночью вас одолело желание позвонить старым знакомым и вы открыли свою телефонную книжку, что собираетесь делать?")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - Внести новый контакт;\n\
    2 - Вывести все контакты;\n\
    3 - Найти контакт;\n\
    4 - Закрыть телефонную книгу.")
    choise = input("Введите цифру: ")
    if choise == '1':
        sep = choice_sep()
        import_data(input_data(), sep)
    elif choise == '2':
        data = export_data()
        print_data(data)
    elif choise == '3':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
        else:
            print("Данные не обнаружены")
    elif choise == '4':
        print('\nХозяин больше не хочет говорить со старыми друзьями?!\n В любом случае, до новых встреч!\n'
              '*шурх-шурх - звук обижено закрывающихся страниц')
        exit()
    print()
    print()
    choice_todo()
