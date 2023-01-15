# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def compr(string):
    temp=string[0]
    out=""
    n=0
    for i in string:
        if temp==i:n=n+1
        else:
             
             out=out+str(n)+temp
             n=1
             temp=i
    out=out+str(n)+temp         
    return out

def restore(inpstr):
    out=''
    for i in range(0,len(inpstr),2):
        multip=int(inpstr[i])
        out=out+inpstr[i+1]*multip
    return out

str1="AAAAAAFDDCCCCCCCAEEEEEEEE"
str2="111112222334445"
print(str1)
print(compr(str1))
print(restore(compr(str1)))
print(str2)
print(compr(str2))
print(restore(compr(str2)))


