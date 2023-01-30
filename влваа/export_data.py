import controler as con

def export_list_empl():
    with open('list of employees.csv','r') as file:
        data = []
        for id in file:
            data.append(id)
    return data

def export_list_empl():
    with open('list of departments.csv','r') as file:
        data = []
        for id in file:
            data.append(id.split())
    return data
