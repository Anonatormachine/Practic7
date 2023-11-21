# 1. Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет
# собой палиндром, т. е. читается одинаково слева направо и справа налево.


def is_palindrome(num): # Функция для проверки, является ли число палиндромом
    num = str(num) # переводим число в строку
    revers_num = ''.join(reversed(num)) # Переворачиваем строку
    return str(num) == revers_num # Сравниваем изначальную строку и перевернутую

def is_prime(num): # Функция для проверки, является ли число простым
    if num < 2: # Если число меньше двух
        return False # То оно не простое
    for i in range(2, num // 2 + 1): # Перебираем всем числа от 2 до n/2
        if num % i == 0: # Если число делится без остатка
            return False # То вернем False, т.к. число не простое
    return True

def find_palindrom(n):
    numbers = []

    for num in range(2, n + 1): # Перебираем числа от 2 до n
        binary = bin(num)[2:] # Получаем двоичное представление числа и убираем '0b' в начале

        if is_palindrome(binary) and is_prime(num): # Проверяем является ли двоичное представление палиндромом и число простым
            numbers.append(num) # Если оба условия выполняются, добавляем число в список

    return numbers


n = int(input("Введите n: ")) # Получаем n из консоли
result = find_palindrom(n) # Вызываем функцию поиска простых палидромов от 2 до n

print(f"Простые палидромромные числа до {n}: {result}")
