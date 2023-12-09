# 1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из цифр а, b, с.


def count_numbers(a, b, c, N):
    count = 0 
    num_list = [str(a), str(b), str(c)]
    for num in range(100, N + 1):
        num_str = str(num) 
        if num_str[0] in num_list and num_str[1] in num_list and num_str[2] in num_list:
            count += 1
    return count 

a = int(input("Введите a:")) 
b = int(input("Введите b:"))
c = int(input("Введите v:"))
N = int(input("Введите N (210 < N < 231):"))

result = count_numbers(a, b, c, N) 
print(f"Количество чисел на отрезке [100, {N}] из цифр {a}, {b}, {c}: {result}")
