# задача 4. Задайте два числа. Напишите программу, которая найдёт НОК(наименьшее общее кратное) этих двух чисел.

def calculate_lcm(x, y): 
    if x > y: 
        greater = x 
    else:
        greater = y 
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1 
    return lcm 
 
num1 = int(input("Введите число 1: ")) 
num2 = int(input("Введите число 2: "))
print(f"НОК для чисел {num1} и {num2} равно {calculate_lcm(num1, num2)}")