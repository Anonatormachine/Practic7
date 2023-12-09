# Даны две дроби A/B и C/D (А, В, С, D — натуральные числа).
# Составить программу вычитания из первой дроби второй.
# Ответ должен быть несократимой дробью. Использовать подпрограмму алгоритма Евклида для определения НОД.

def euclid_algorithm(a, b): 
    while b:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D): 
    gcd = euclid_algorithm(numerator, denominator) 

    numerator //= gcd 
    denominator //= gcd 

    return numerator, denominator

A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
D = int(input("Введите D: "))

numerator, denominator = subtract_fractions(A, B, C, D)

print(f"Результат вычитания дробей {A}/{B} - {C}/{D}: {numerator}/{denominator}")
