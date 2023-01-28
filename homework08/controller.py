# Основное дз(из семинара):
# Создать информационную систему позволяющую работать с учениками школы
# функции
# 1 Добавление нового студента (Поля - имя, фамилия)
# 2 Добавление предмета (добавляется всем ученикам сразу)
# 3 Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )
# 4 Показ списка учеников (имена фамилия)
# 5 Показ листа оценок конкретного ученика
# 6 Выход из программы
# Достаточно хранить данные в переменной

# Доп*:
# 1) Добавить функцию генерации сразу ста учеников и записи их в журнал
# (имя - рандомное из списка нескольких имен
# фамилия - рандомная из списка нескольких фамилий
# название предмета - рандом из списка с предметами
# оценка - рандом от 1 до 5)
# 2) Вывод средней оценки ученика по одному предмету
# 3) Вывод среднего балла по школе по конкретному предмету
# 4) Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
# Добавить хранение в файле, и импорт из файла
import imports
import view
import export

def start():
    print(" 1 - Добавление нового студента \n 2 - Добавление предмета\n 3 - Добавление оценки ученику по предмету \n 4 - Показ списка учеников \n"
    " 5 - Показ листа оценок конкретного ученика\n 6 - выход \n 7 - ДОП. ")
    while(True):
        
        n=int(input("введите команду: "))
        if n==1:
            export.add_student()
        elif n==2: 
            export.add_theme()
        elif n==3:
            export.add_mark()
        elif n==4:
            view.show_students()
        elif n==5:
            view.show_marks()
        elif n==6:
            break
        elif n==7:
            print(" 1 - Добавить 100 учеников \n 2 - Вывод средней оценки ученика по предмету\n 3 - Вывод среднего балла \n"
            " 4 - Вывод количества учеников претендующих на золотую медаль \n 5 - Возврат в основное меню ")
            n=int(input("введите команду: "))
            if n==1:
                export.generate_students()
            elif n==2: 
                view.show_sr()
            elif n==3:
                view.show_sr_all()
            elif n==4:
                view.show_gold()
            elif n==5:
                view.show_marks()
            elif n==6:
                break
            

start()