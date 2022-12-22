# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec=int(input())
bin=''
while(True):
    ost=dec%2
    dec=int(dec/2)
    bin=str(ost)+bin
    if(dec==0):break

print(bin)