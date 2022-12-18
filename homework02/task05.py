# Реализуйте алгоритм перемешивания списка.

import random

def shuff (list1):

    for i in range(0,len(list1)):
        index=random.randint(0, len(list1)-1)
        temp=list1[i]
        list1[i]=list1[index]
        list1[index]=temp
    

list1=[1,2,3,4,5,6,7,8,9,10]
#random.shuffle(list1)
shuff(list1)
print(list1)