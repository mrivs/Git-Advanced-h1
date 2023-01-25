# модуль контроллер
import m_import
import export
import sort
import view

def start():
    print(" 1 - ввести новые данные \n 2 - просмотр данных\n 3 - вывести ФИ \n 4 - сортировка по ИД \n 5 - сортировка по имени\n 6 - выход ")
    while(True):
        
        n=int(input("введите команду: "))
        if n==1:
            export.add_data()
        elif n==2: 
            m_import.print_data()
        elif n==3:
            view.view_names()
        elif n==4:
            sort.sort_id()
        elif n==5:
            sort.sort_name()
        elif n==6:
            break
