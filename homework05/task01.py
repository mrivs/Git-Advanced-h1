# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет. 
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил.

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#   a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 1 до 28)
#   b) Подумайте как наделить бота "интеллектом" 
#   (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

import random

status=lambda N,pl:print (f"Конфет осталось: {N}. Ходит игрок {pl}:", end=" ")

def take_sweet(Konf):
    while(True):
     command=input()
     if command=="q":
        Konf=-100
        break
     count=int(command)
     if 0< count <29: 
        Konf=Konf-count
        break
     print("Можно брать от 1 до 28 конфет")
    return Konf

def pc_take_sweet(Konf,max):
    value=Konf%(max+1)
    if value==0:value=random.randint(1, 28)
    Konf=Konf-value
    print(value)
    return Konf

def change_pl(pl):
    if pl==1:pl=2
    else:pl=1
    return pl

def hum_game():
    Konf=221
    pl=random.randint(1, 2)
    print(f"Первый ходит {pl} игрок ")
    while(Konf>0):
        status(Konf,pl)

        Konf=take_sweet(Konf)
        if -30<Konf<1: print(f"Игрок {pl} выйграл")
        if Konf==-100: print("Игра прервана")
        pl=change_pl(pl)
    
def pc_game():
    Konf=221
    pl=random.randint(1, 2)
    print(f"Первый ходит {pl} игрок ")
    while(Konf>0):
        
        if pl==1:
            status(Konf,pl)
            Konf=take_sweet(Konf)
        else:
            status(Konf,"2 (ПК)") 
            Konf=pc_take_sweet(Konf,28)
        if -30<Konf<1: print(f"Игрок {pl} выйграл")
        if Konf==-100: print("Игра прервана")
        pl=change_pl(pl)
    
print("Игра в конфеты: \n 1 - человек-человек \n 2 - человек - ПК")
num=int(input())
if num==1:hum_game()
elif num==2:pc_game()
