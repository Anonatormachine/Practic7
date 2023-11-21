# Даны две дроби A/B и C/D (А, В, С, D — натуральные числа).
# Составить программу вычитания из первой дроби второй.
# Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД.

def euclid_algorithm(a, b): # Алгоритм Евклида для нахождения НОД
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D): # Вычитание дробей A/B - C/D
    numerator = A * D - C * B # Находим числитель частного дробей путем умножение на знаменатели. A умножаем на знаменательно другой дроби
    denominator = B * D # Находим общий знаменатель путем перемножения двух знаменателей

    gcd = euclid_algorithm(numerator, denominator) # Находим НОД для числителя и знаменателя

    numerator //= gcd # Делим числитель на нод
    denominator //= gcd # Делим знаменатель на нод

    return numerator, denominator

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

numerator, denominator = subtract_fractions(A, B, C, D)

print(f"Результат вычитания дробей {A}/{B} - {C}/{D}: {numerator}/{denominator}")
