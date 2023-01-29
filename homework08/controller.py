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
import interface
import database
import random
scdata={}
students=["кот"]
lessons=["мат"]
for st in students:scdata[st]={}
for name in students:
               for l in lessons: scdata[name][l]=[]

def add_student(name):
    global scdata,students,lessons
    if name not in students:
        students.append(name)
        scdata[name]={}
        for lesson in lessons:
            scdata[name][lesson]=[]
        return True
    else: return False

def add_lesson(lesson):
    global scdata,students,lessons
    if lesson not in lessons:
        lessons.append(lesson)
        for name in students:
            scdata[name][lesson]=[]
        return True
    else: return False

def start():
    
    while(True):
        print(interface.menu)
        n=int(input("введите команду: "))
        if n==1:
            name=interface.input_student()
            if not add_student(name):print("имя уже есть!")

        elif n==2:  
            lesson=interface.input_lesson()
            if not add_lesson(lesson):print("предмет уже есть!")
       
        elif n==3:
            name,lesson,mark=interface.input_mark()
            scdata[name][lesson].append(mark)
            
        elif n==4:
            for stud, less in scdata.items(): 
                print (stud,less)

        elif n==5:
            name=interface.input_student()
            print(scdata[name])

        elif n==6:
            break
        elif n==7: 
            print(interface.submenu)
            n=int(input("введите команду: "))
            if n==1: # заполняем базу ранд. учениками предметами и оценками
                k=0
                while (k<10):
                    name=database.get_rand_name()
                    if add_student(name): k+=1
                k=0
                while (k<2):
                    less=database.get_rand_less()
                    if add_lesson(less): k+=1
                for name in students:
                    for lesson in lessons:
                        for i in range(1,4):    
                            scdata[name][lesson].append(random.randint(3,5)) # без двоек

            elif n==2: 
                name=interface.input_student()
                lesson=interface.input_lesson()
                if name not in students or lesson not in lessons: print("Неправильный запрос")
                else: 
                    line=scdata[name][lesson]
                    sr=float (sum(line)/len(line))
                    print (f"Средняя оценка ученика {name} по предмету {lesson}: {sr:.2f}")

            elif n==3:

                
                view.show_sr_all()
            elif n==4:
                view.show_gold()
            
            elif n==6:
                break
            


