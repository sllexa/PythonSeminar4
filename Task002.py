# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

def fill_list(num) -> list:
    u_list = []
    for i in range(num):
        u_list.append(randint(0, num))
    return u_list

def unique_values_list(u_list):
    new_list = []
    for i in u_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

num = int(input("Введите размер последовательности: "))
user_list = fill_list(num)
print(user_list)
print(unique_values_list(user_list))