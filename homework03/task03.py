# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fr_part(value):
    return abs(value-int(value))

def func(array):
    max=fr_part(array[0])
    min=fr_part(array[0])

    for i in range(1,len(array)):
        if fr_part(array[i])>max:max=fr_part(array[i])
        if min==0:min=fr_part(array[i])
        if fr_part(array[i])!=0 and fr_part(array[i])<min:min=fr_part(array[i])
    return round((max-min),14)

array=[1.1, 1.2, 3.1, 5, 10.01] 
print (func(array))