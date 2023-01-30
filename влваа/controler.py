from user_interface import *
import import_data as imda
import export_data as ed

all_departments = {}
all_employees = {}
department_employees = {}
id_employees = 1

def choose_todo(choose_user):
    if choose_user == '1':
        print('Список всех сотрудников: ')
        print(*ed.export_list_empl())
        user_menu()
    # elif choose_user == '2':
    #     # TODO добавить менюшку с общей инфой
    #     choose_user = input('''Выберите какую информацию вы хотите получить?
    #                         1. Список отделов и количество сотрудников;
    #                         2. Информацию о сотрудниках отдела;''')
    #     # TODO сделать возвратку к этой функции
    elif choose_user == '3':
        create_department()
    elif choose_user == '4':
        add_employees()
    elif choose_user == '5':
        change_employee_info(edit_empl_id())
    elif choose_user == '6':
        employee_transfer(edit_empl_id())
    elif choose_user == '7':
        delete_info_employee()
    elif choose_user == '8':
        disband_department()
    elif choose_user == '9':
        end()
    else:
        print('Похоже, вы решили сделать что-то, что мне недоступно, пожалуйста повторите свой выбор')
        user_menu()



def create_department(name_department = False): # Создание отдела
    if not name_department:
        name_department = input("Введите название отдела: ")
        all_departments[name_department] = []
        print('Отличная новость, благодаря вам, в комании открылся новый отдел!!Так держать!')

def add_employees(): # Добавление нового сотрудника
    surname = input("Введите фамилию сотрудника: ")
    name = input("Введите имя сотрудника: ")
    patronymic = input("Введите отчество сотрудника: ")
    birth = input("Введите дату рождения сотрудника: ")
    tel = input("Введите номер телефона сотрудника: ")
    adress = input("Введите адрес сотрудника: ")
    post = input("Введите должность, занимаемую сотрудником: ")
    department = input('Введите отдел, в котором будет работать сотрудник: ')
    if department not in all_departments:
        create_department(department)
    global id_employees
    all_departments[department].append(str(id_employees))
    all_employees[str(id_employees)] = [surname,name,patronymic,birth,tel,adress,post,department]
    id_employees += 1

    imda.import_list_empl(all_employees)
    imda.import_list_departments(all_departments)


def edit_empl_id():
    empl_id = int(input('Введите id работника, информацию о котором хотите изменить: '))
    if empl_id in all_employees:
        return empl_id
    else:
        print('Работника с таким id не существует, повторите ввод!')
        edit_empl_id()


def change_employee_info(emplooyee_id): # Изменение информации о сотруднике
    print(f"Укажите новые данные о сотруднике: \n{all_employees[emplooyee_id]}")
    old_info = [all_employees[emplooyee_id]]
    surname = input("Введите фамилию сотрудника: ")
    name = input("Введите имя сотрудника: ")
    patronymic = input("Введите отчество сотрудника: ")
    birth = input("Введите дату рождения сотрудника: ")
    tel = input("Введите номер телефона сотрудника: ")
    adress = input("Введите адрес сотрудника: ")
    post = all_employees[emplooyee_id]
    new_info = [surname, name, patronymic, birth, tel, adress, post]
    all_employees[emplooyee_id] = new_info

    imda.edit_import_list_empl(all_employees)

def employee_transfer(emplooyee_id): # Перевод сотрудника в другой отдел
    old_department = all_employees[emplooyee_id][-1]
    new_department = input('Введите название нового отдела: ')
    if new_department not in all_departments:
        create_department(new_department)
    all_departments[old_department].remove(emplooyee_id)
    all_departments[new_department].append(emplooyee_id)

    imda.edit_import_list_departments(all_departments)
    imda.edit_import_list_empl(all_employees)

def delete_info_employee(emplooyee_id):
    old_department = all_employees[emplooyee_id][-1]
    all_departments[all_employees[emplooyee_id][-1]].remove(emplooyee_id)
    del all_departments[emplooyee_id]

    imda.edit_import_list_departments(all_departments)
    imda.edit_import_list_empl(all_employees)

def disband_department():
    pass

def end():
    print("Вы решили, что и так слишком много сегодня работали, "
          "потому, закрыли книжку и отправились домой")
    exit()

# def search_data(word, data): # Для поиска конкретного сотрудника
#     if len(data) > 0:
#         for item in data:
#             if word in item:
#                 return item
#     else:
#         return None