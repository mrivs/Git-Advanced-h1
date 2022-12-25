# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N=int(input("Введите N: "))
d=2
list1=[]
while(True):
    if (N%d!=0):d=d+1
    else:
        list1.append(d)
        N=N/d

    if d>N:break
print(list1)