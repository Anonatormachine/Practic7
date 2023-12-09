# 1. Найти все простые натуральные числа, не превосходящие n, двоичная запись которых представляет
# собой палиндром, т. е. читается одинаково слева направо и справа налево.


def is_palindrome(num): 
    num = str(num)
    revers_num = ''.join(reversed(num))
    return str(num) == revers_num 

def is_prime(num):
    if num < 2: 
        return False 
    for i in range(2, num // 2 + 1): 
        if num % i == 0: 
            return False 
    return True

def find_palindrom(n):
    numbers = []

    for num in range(2, n + 1):
        binary = bin(num)[2:] 

        if is_palindrome(binary) and is_prime(num):
            numbers.append(num) 

    return numbers


n = int(input("Введите n: ")) 
result = find_palindrom(n) 

print(f"Простые палидромромные числа до {n}: {result}")
