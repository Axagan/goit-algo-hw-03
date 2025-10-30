import random

def get_numbers_ticket(min_val, max_val, quantity):
 
    # Перевірка валідності вхідних даних
    if not (1 <= min_val <= max_val <= 1000):
        return []
    if not (1 <= quantity <= (max_val - min_val + 1)):
        return []

    # Генеруємо унікальні числа за допомогою random.sample
    numbers = random.sample(range(min_val, max_val + 1), quantity)

    # Сортуємо числа перед поверненням
    numbers.sort()
    return numbers


# Приклади використання
print(get_numbers_ticket(1, 49, 6))   # Наприклад, для класичної лотереї 6 з 49
print(get_numbers_ticket(1, 36, 5))   # Лотерея 5 з 36
print(get_numbers_ticket(1, 10, 10))  # Всі числа від 1 до 10
print(get_numbers_ticket(1, 5, 6))    # Некоректні параметри → поверне []
