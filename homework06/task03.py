# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
array1 = [2, 3, 6, 4, 5]
array2 = [2, 3, 4, 5]

pr=lambda li:[ li[i]*li[-i-1] for i in range(int((len(li))/2+0.6))]
print(pr(array1))
print(pr(array2))