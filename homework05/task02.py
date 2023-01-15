# 39(2). Создайте программу для игры в ""Крестики-нолики"".
# Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту
# (как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), 
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу
# ( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)


draw=lambda arr:print(f"{arr[0]}|{arr[1]}|{arr[2]}\n{arr[3]}|{arr[4]}|{arr[5]}\n{arr[6]}|{arr[7]}|{arr[8]}")
status=lambda pl:print (f"Ходит {pl}:", end=" ")

def change_pl(pl):
    if pl=="X":pl="O"
    else:pl="X"
    return pl

def chek_win(arr):
    win=" "
    wins = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for pos in wins:
        if arr[pos[0]] == arr[pos[1]] ==arr[pos[2]]: 
            win= arr[pos[0]]
            break
    return win
    
arr=["1","2","3","4","5","6","7","8","9"]
n=0
draw(arr)

for i in range(0,9):arr[i]=" "
pl="X"

while(n<9):
    status(pl)
    while(True):
        num=int(input())
        num=num-1
        if arr[num]==" ":
            arr[num]=pl
            break
        else: 
            print("неверная позиция")
            status(pl)
    
    draw (arr)
    if chek_win(arr)!=" ": 
        print(f"Игрок {pl} победил")
        break
    pl=change_pl(pl)
    n=n+1
    if n==9:print("ничья")