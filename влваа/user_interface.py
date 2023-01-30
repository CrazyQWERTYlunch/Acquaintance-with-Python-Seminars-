import controler as con



def user_menu():
    print('Перед вами справочник компании, что вы хотите сделать?')
    user_choose = input('''1. Посмотреть список всех сотрудников;
2. Посмотреть информацию по отделам;
3. Добавить отдел;
4. Добавить нового сотрудника;
5. Изменить личную информацию о сотруднике;
6. Перевести сотрудника в другой отдел;
7. Уволить сотрудника и удалить информацию о нем;
8. Расформировать отдел;
9. Закрыть справочник и пойти домой.
Что вы выберете?''')
    con.choose_todo(user_choose)
user_menu()
    # 1. Просмотр списка всех сотрудников (id: Имя/фамилия/Отчество/год_рождения/Номер телефона/Должность/отдел)
    # 2. Просмотр информации по отделам (общее количество отделов,общее количество сотрудников)
    #     2.1. Список отделов (Список отделов, название,количество сотрудников)
    #     2.2. Сотрудники отдела (выбор отдела, список сотрудников)
    # 3. Добавить отдел
    # 4. Добавить нового сотрудника
    # 4. Изменить информацию о сотруднике
    # 5. Перевести сотрудника в другой отдел
    # 6. Удалить информацию о сотруднике
    # 7. Расформировать отдел и всех его сотрудников

