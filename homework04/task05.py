# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def getdictionary(poly):
    dictp={}
    poly=poly.strip()
    listp=poly.split("=")
    poly=listp[0]
    listp=poly.split("+")

    for i in range(len(listp)):
    
        if listp[i].find("*x**")!=-1:
            arr=(listp[i].split("*x**"))
            dictp[int(arr[1])]=int(arr[0])

        elif listp[i].find("x**")!=-1:
            arr=(listp[i].split("x**"))
            dictp[int(arr[1])]=1

        elif listp[i].find("*x")!=-1:
            arr=(listp[i].split("*x"))
            dictp[1]=int(arr[0])

        elif listp[i].find("x")!=-1:
            dictp[1]=1
        else:dictp[0]=(int(listp[i]))
    return dictp



with open('homework04/polynomial_1.txt', 'r') as data:
    poly1=data.readline()
with open('homework04/polynomial_2.txt', 'r') as data:
    poly2=data.readline()

dict1=getdictionary(poly1)
dict2=getdictionary(poly2)

print(dict1)
print(dict2)





