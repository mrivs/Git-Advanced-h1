# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

value=float(input())
value=abs(value)
sum=0
s=str(value).split('.')
for i in [0,1]:
    for (j) in s[i]: sum=sum+int(j)
print (sum)