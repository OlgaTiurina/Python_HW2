# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# - Для n = 15:  Ответ: 3
# - Для n = 35:  Ответ: 5

n = int(input("Введите целое число N: "))
i = 2
while n % i != 0:
    i += 1
print(f"Наименьший натуральный делитель целого числа {n} равен: {i}")
