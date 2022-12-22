# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def func_calc(array):
    list1 = []

    for i in range(int((len(array))/2+0.6)):
        pr = array[i]*array[len(array)-1-i]
        list1.append(pr)
    return list1


array1 = [2, 3, 4, 5, 6]
array2 = [2, 3, 5, 6]
print(func_calc(array1))
print(func_calc(array2))
