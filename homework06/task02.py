# 45. Найти сумму чисел списка стоящих на нечетной позиции

array=[2,3,5,9,3,7]
summ=lambda li:sum([v for i,v in enumerate(li) if i%2!=0])
print(summ (array))



