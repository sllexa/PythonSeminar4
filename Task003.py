# задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def write_file(st):
    with open('task003.txt', 'w') as data:
        data.write(''. join(st))

def create_factor(k) -> list:
    new_list = []
    for i in range(1, k + 2):
        new_list.append(randint(0, 100))
    return new_list

def create_str(k: int, factor: list) -> list:
    result = []
    for i in range(len(factor)):
        if k == 1:
            result.append(f"{factor[i]} * x")
        elif k == 0:
            result.append(f"{factor[i]}")
        else:
            result.append(f"{factor[i]} * x ^ {k}")
        signs = randint(0, 1)
        if signs == 1: result.append(" + ")
        elif signs == 0: result.append(" - ")
        k -= 1
    result.pop(-1)
    result.append(" = 0")
    return result

k = int(input("Введите степень k: "))
factor = create_factor(k)
write_file(create_str(k, factor))
print(''.join(create_str(k, factor)))
