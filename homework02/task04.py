# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

with open('homework02/file.txt', 'w') as data: # запишем файл file.txt с позициями 0,1,4
 data.write('0\n')
 data.write('1\n')
 data.write('4\n')

n=int(input("введите N "))
list_numbers=[i for i in range(-n,n+1)]
print('Список: ',list_numbers)

with open('homework02/file.txt', 'r') as data: # читаем файл file.txt с позициями
    list_pos= [int(line) for line in data]
print ('Индексы: ',list_pos)

value=1
for i in list_pos:
    if i<len(list_numbers): value=value*list_numbers[i]
    else: print('Индекс превышает размер сиска')
print('Ответ: ',value)