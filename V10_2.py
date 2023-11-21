# 2. Составить программу, которая изменяет последовательность слов в строке на обратную.


def reverse_words(text):
    words = text.split() # Делим строку на массив слов
    words.reverse() # Переворачиваем массив слов
    reversed_text = ' '.join(words) # Соединяем слова в строку
    return reversed_text


text = input("Введите строку: ") # Получаем строку из консоли
reversed_text = reverse_words(text) # Вызываем функцию переворота слов

print("Исходная строка:", text)
print("Строка с обратным порядком слов:", reversed_text)