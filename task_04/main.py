# 4. Напишите программу, которая принимает на вход 2 числа. Задайте 
# список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15
length = int(input("Введите число N : "))
arr = []
for i in range((-length),length + 1):
    arr.append(i)
print(f"Список чисел от {-length} до {length}\n {arr}")
pos_a = int(input("Введите первую позицию : "))
pos_b = int(input("Введите вторую позицию : "))
if (pos_a > length*2+1 or pos_a > length*2+1 ):
    print("Одна из заданных позиций больше, чем всего позиций")
    exit()
print(f'Произведение чисел позиций {pos_a}(число {arr[pos_a-1]}) и {pos_b}(число {arr[pos_b-1]}) равно {arr[pos_a-1] * arr[pos_b-1]}')