# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def get_one(array):
    dict = {}
    list1 = []
    for i in range(len(array)):
        if dict.get(array[i]) != None:
            dict[array[i]] = dict[array[i]]+1
        else:
            dict[array[i]] = 1

    for key in dict:
        if dict[key] == 1:
            list1.append(key)

    return (list1)


array = [ 33,11, 33, 33, 22, 22, 1, ]
print(get_one(array))
