# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def getdictionary(poly): # получаем словарь из строковой записи многочлена ключ(степень одночлена)  значение(коэффициент одночлена)
    dictp = {}
    poly = poly.strip()
    listp = poly.split("=")
    poly = listp[0]
    listp = poly.split("+")

    for i in range(len(listp)):

        if listp[i].find("*x**") != -1:
            arr = (listp[i].split("*x**"))
            dictp[int(arr[1])] = int(arr[0])

        elif listp[i].find("x**") != -1:
            arr = (listp[i].split("x**"))
            dictp[int(arr[1])] = 1

        elif listp[i].find("*x") != -1:
            arr = (listp[i].split("*x"))
            dictp[1] = int(arr[0])

        elif listp[i].find("x") != -1:
            dictp[1] = 1
        else:
            dictp[0] = (int(listp[i]))
    return dictp

def getsumkof(dict1,dict2): # складываем словари и возвращаем упорядоченый лист коэффциентов
    max=0
    dict3 = dict1 | dict2
    for key in dict3:
        if key>max:max=key
        if dict1.get(key) != None and dict2.get(key)!=None:
            dict3[key] = dict2[key]+dict1[key]

    kof=[0]*(max+1)
    for key in dict3:
        kof[key]=dict3[key]
    kof.reverse()
    return(kof)

def writepoly(kof): # записываем многочлен в строку по листу коэффициентов
    listp=[]
    for i in range(len(kof)):
        deg=len(kof)-i-1      # степень одночлена    
        if kof[i] != 0:
            if (deg)==0: listp.append(str(kof[i]))
            elif(deg)==1 and kof[i]==1:listp.append('x')
            elif(deg)==1:listp.append(str(kof[i])+'*x')
            elif kof[i]==1:listp.append('x**'+str(deg))
            else: listp.append(str(kof[i])+'*x**'+str(deg))
    if listp==[]:listp="0"
    poly=" + ".join(listp)+" = 0"
    return(poly)


with open('homework04/polynomial_1.txt', 'r') as data:
    poly1 = data.readline()
with open('homework04/polynomial_2.txt', 'r') as data:
    poly2 = data.readline()

dict1 = getdictionary(poly1)
dict2 = getdictionary(poly2)
kof=getsumkof(dict1,dict2)

poly=writepoly(kof)

print(poly1)
print(poly2)
print(poly)
with open('homework04/polynomial_sum.txt', 'w') as data:
     data.write(poly)