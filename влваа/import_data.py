import controler as con

def import_list_empl(list_eplo):
    with open('list of employees.csv','a+', encoding='utf=8') as file:
        for elem in list_eplo:
            file.write(f"{elem} {' '.join(list_eplo[elem])}\n")
# todo: прописать параметры

def edit_import_list_empl(list_eplo):
    with open('list of employees.csv','w', encoding='utf=8') as file:
        for elem in list_eplo:
            file.write(f"{elem} {' '.join(list_eplo[elem])}\n")

def import_list_departments(list_dep):
        with open('list of departments.csv', 'a+', encoding='utf=8') as file:
            for elem in list_dep:
                file.write(f"{elem} {' '.join(list_dep[elem])}")


def edit_import_list_departments(list_dep):
    with open('list of departments.csv', 'w', encoding='utf=8') as file:
        for elem in list_dep:
            file.write(f"{elem} {' '.join(list_dep[elem])}")
