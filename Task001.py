# задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def fill_list(n) -> list:
    s_list = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            s_list.append(p)
            n //= p
        else:
            p += 1
    s_list.append(n)
    return s_list

n = int(input("Введите натуральное число: "))
s_list = fill_list(n)
print(s_list)
