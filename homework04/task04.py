# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input("задайте степень многочлена k = "))
kof = []                  # список коэффициентов
listp=[]                  # список одночленов

for i in range(k+1):
    kof.append(random.randint(0, 100))
print(kof)

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
print(poly)

with open('homework04/polynomial_0.txt', 'w') as data:
     data.write(poly)
