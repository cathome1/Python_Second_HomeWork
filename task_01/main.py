# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input('Введите число : '))
int_num = num * (10 ** (len(str(num)) - 2) )
count = 0
while (int_num > 0):
    count += int_num % 10
    int_num = int_num // 10
print(f'Сумма цифр числа {num} равна {int(count)}')
