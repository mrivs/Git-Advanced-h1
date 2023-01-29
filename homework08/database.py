#данные
import random

names="Клим,Пётр,Матвей,Владимир,Михаил,Семён,Степан,Александр,Влад,Сергей,Артём,Илья,Данила,Руслан,Иван,Олег,Мирослав,Кирилл,Алексей,Вадим"
snames="Новиков,Мельников,Михайлов,Иванов,Медведев,Иванов,Измайлов,Кузнецов,Климов,Маслов"
"Иванов,Чистяков,Колесников,Денисов,Кондратов,Исаев,Соколов,Медведев,Грачев,Кононов"
less="Физика,Химия,Русский язык,Английский язык,История,Информатика,Технология,Алгебра,Геометрия,Литература,Музыка"

def rand_name(names,snames):
    listnames=names.split(",")
    listsnames=snames.split(",")
    n=random.choice(listnames)
    sn=random.choice(listsnames)
    return(n+" "+sn)

def get_rand_name():
    return rand_name(names,snames)

def get_rand_less():
    listless=less.split(",")
    return random.choice(listless)


print(get_rand_name())