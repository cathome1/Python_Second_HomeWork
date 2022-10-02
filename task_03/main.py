# 3. Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
import math
length = int(input('Введите размер списка : '))
res = 0
arr = []
for i in range(1,length + 1):
    arr.append(round((1+1/i)**i))
    res += arr[i - 1]
print(f"Сумма чисел списка - {arr} равна {res}")