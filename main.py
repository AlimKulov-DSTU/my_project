print('Hello, GitHub!')
import random
#Циклы

# Таблица умножения
print("=" * 50)
print("1. Таблица умножения:")
print("   ", end="")
for i in range(1, 10):
    print(f"{i:4}", end="")
print("\n" + "-" * 40)

for i in range(1, 10):
    print(f"{i} |", end="")
    for j in range(1, 10):
        print(f"{i*j:4}", end="")
    print()

# Сумма нечётных чисел
print("\n" + "=" * 50)
print("2. Сумма нечётных чисел от 1 до 100:")
sum_odd = 0
for i in range(1, 101, 2):
    sum_odd += i
print(f"Результат: {sum_odd}")

# Делители числа
print("\n" + "=" * 50)
print("3. Поиск делителей числа:")
n = int(input("Введите число: "))
print(f"Делители числа {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# Факториал
print("\n" + "=" * 50)
print("4. Вычисление факториала:")
n = int(input("Введите число для вычисления факториала: "))
factorial = 1
if n < 0:
    print("Факториал отрицательного числа не определен")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал числа {n} = {factorial}")

# Фибоначчи
print("\n" + "=" * 50)
print("5. Последовательность Фибоначчи:")
n = int(input("Введите длину последовательности: "))
if n <= 0:
    print("Длина должна быть положительным числом")
else:
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print("Последовательность Фибоначчи:")
    print(" ".join(map(str, fib_sequence)))

#Списки

print("=" * 60)
print("РАБОТА СО СПИСКАМИ")
print("=" * 60)

# 0. Генерация базового списка
numbers = [random.randint(-50, 50) for _ in range(10)]
print(f"0. Сгенерированный список: {numbers}")

# 1. Чётные элементы
print("\n" + "=" * 40)
print("1. Чётные элементы:")
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Чётные числа: {even_numbers}")

# 2. Максимум и минимум
print("\n" + "=" * 40)
print("2. Максимальное и минимальное число:")
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"Максимум: {max_num}, Минимум: {min_num}")

# 3. Ввод чисел пользователем
print("\n" + "=" * 40)
print("3. Ввод 5 чисел пользователем:")
user_numbers = []
for i in range(5):
    num = int(input(f"Введите число {i+1}: "))
    user_numbers.append(num)
user_numbers.sort()
print(f"Отсортированный список: {user_numbers}")

# 4. Удаление дубликатов
print("\n" + "=" * 40)
print("4. Удаление дубликатов:")
numbers_with_duplicates = [random.randint(-10, 10) for _ in range(15)]
print(f"Список с дубликатами: {numbers_with_duplicates}")
unique_numbers = []
for num in numbers_with_duplicates:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"Без дубликатов: {unique_numbers}")

# 5. Замена первого и последнего элемента
print("\n" + "=" * 40)
print("5. Замена первого и последнего элемента:")
numbers_for_swap = [random.randint(-50, 50) for _ in range(10)]
print(f"До замены: {numbers_for_swap}")
if len(numbers_for_swap) >= 2:
    numbers_for_swap[0], numbers_for_swap[-1] = numbers_for_swap[-1], numbers_for_swap[0]
    print(f"После замены: {numbers_for_swap}")
else:
    print("Список слишком короткий")

#Словари

print("=" * 60)
print("РАБОТА СО СЛОВАРЯМИ")
print("=" * 60)

# 1. Словарь студентов и средний балл
print("\n" + "=" * 40)
print("1. Словарь студентов и средний балл:")

students = {
    "Кулов": 4,
    "Ежов": 5,
    "Зиновьев": 3,
    "Ульянов": 4
}

print("Студенты и оценки:")
for name, grade in students.items():
    print(f"{name}: {grade}")

total = sum(students.values())
average = total / len(students)
print(f"\nСредний балл: {average:.2f}")

# 2. Подсчет букв в строке
print("\n" + "=" * 40)
print("2. Подсчет букв в строке:")

text = input("Введите строку для анализа: ")
letter_count = {}

for char in text:
    if char.isalpha():
        char_lower = char.lower()
        letter_count[char_lower] = letter_count.get(char_lower, 0) + 1

print("\nКоличество каждой буквы:")
if letter_count:
    for letter, count in sorted(letter_count.items()):
        print(f"'{letter}': {count}")
else:
    print("В строке нет букв")

# 3. Словарь чисел и их квадратов
print("\n" + "=" * 40)
print("3. Словарь чисел и их квадратов:")

squares_dict = {}
for i in range(1, 11):
    squares_dict[i] = i ** 2

print("Число → Квадрат:")
for number, square in squares_dict.items():
    print(f"{number} => {square}")

# 4. Словарь из двух списков
keys_list = ["имя", "возраст", "город", "профессия"]
values_list = ["Рамазан", 21, "Москва", "Налоговый инспектор"]

if len(keys_list) == len(values_list):
    result_dict = dict(zip(keys_list, values_list))
    print("Словарь созданный через zip():")
    for key, value in result_dict.items():
        print(f"{key}: {value}")
else:
    print("Списки разной длины!")

#Множества

print("=" * 60)
print("РАБОТА С МНОЖЕСТВАМИ")
print("=" * 60)

# 1. Пересечение и объединение
print("\n" + "=" * 40)
print("1. Пересечение и объединение множеств:")

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {7, 8, 9, 10, 11, 12, 13, 14, 15}

print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")
print(f"Пересечение: {set1 & set2}")
print(f"Объединение: {set1 | set2}")
print(f"Разность (1-2): {set1 - set2}")
print(f"Симметрическая разность: {set1 ^ set2}")

# 2. Уникальные слова в тексте
print("\n" + "=" * 40)
print("2. Уникальные слова в тексте:")

text = input("Введите текст: ")
words = text.lower().split()
clean_words = [word.strip('.,!?;:()""') for word in words]
unique_words = set(clean_words) #преобразование в множество, множество автоматически удаляет дубликаты

print(f"Уникальные слова: {sorted(unique_words)}")
print(f"Всего уникальных слов: {len(unique_words)}")

# 3. Общие элементы двух списков
print("\n" + "=" * 40)
print("3. Общие элементы двух списков:")

list1 = [77, 36, 84, 88, 4, 8]
list2 = [4, 34, 75, 77, 8, 36]

print(f"Список 1: {list1}")
print(f"Список 2: {list2}")

common_elements = set(list1) & set(list2)
print(f"Общие элементы: {common_elements}")

# 4. Проверка подмножества
print("\n" + "=" * 40)
print("4. Проверка подмножества:")

set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {2, 4, 6, 8}
set_c = {10, 11}

print(f"A: {set_a}")
print(f"B: {set_b}")
print(f"C: {set_c}")

print(f"B ⊆ A: {set_b.issubset(set_a)}")
print(f"C ⊆ A: {set_c.issubset(set_a)}")
print(f"A ⊆ B: {set_a.issubset(set_b)}")

# 5. Удаление элементов меньше заданного числа
print("\n" + "=" * 40)
print("5. Удаление элементов меньше заданного числа:")

numbers_set = {5, 12, 3, 8, 20, 1, 15, 7, 10, 25, 2}
print(f"Исходное множество: {numbers_set}")

threshold = int(input("Введите пороговое число: "))
filtered_set = {x for x in numbers_set if x >= threshold}

print(f"Числа ≥ {threshold}: {filtered_set}")

#Комбинированные задания

print("=" * 60)
print("КОМБИНИРОВАННЫЕ ЗАДАНИЯ")
print("=" * 60)

# 1. Уникальные значения
print("\n" + "=" * 40)
print("1. Уникальные значения из случайных чисел:")

numbers = [random.randint(1, 15) for _ in range(20)]
print(f"Исходный список: {numbers}")
unique_numbers = list(set(numbers))
print(f"Уникальные значения: {sorted(unique_numbers)}")

# 2. Словарь частот
print("\n" + "=" * 40)
print("2. Словарь частот элементов:")

numbers = [random.randint(1, 10) for _ in range(15)]
print(f"Список: {numbers}")
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print("Частота:")
for num, count in sorted(frequency.items()):
    print(f"  {num}: {count}")

# 3. Множество длинных слов
print("\n" + "=" * 40)
print("3. Множество длинных слов:")

words = ["энтропия", "ячейка", "слово", "дом", "иж", "множество"]
print(f"Слова: {words}")
long_words = {word for word in words if len(word) > 5}
print(f"Слова > 5 символов: {long_words}")

# 4. Частота слов в предложении
print("\n" + "=" * 40)
print("4. Частота слов в предложении:")

sentence = input("Введите предложение: ")
words = sentence.lower().split()
clean_words = [word.strip('.,!?;:()""') for word in words]
word_count = {}
for word in clean_words:
    word_count[word] = word_count.get(word, 0) + 1
print("Частота слов:")
for word, count in sorted(word_count.items()):
    print(f"  '{word}': {count}")

# 5. Удаление дубликатов
print("\n" + "=" * 40)
print("5. Удаление дубликатов через множество:")

numbers = [random.randint(1, 10) for _ in range(15)]
print(f"С дубликатами: {numbers}")
unique = list(set(numbers))
print(f"Без дубликатов: {sorted(unique)}")

# 6. Самый дорогой товар
print("\n" + "=" * 40)
print("6. Самый дорогой товар:")

products = {"газировка": 50, "выпечка": 150, "мясо": 300, "икра": 5000}
print("Товары:")
for product, price in products.items():
    print(f"  {product}: {price} руб.")
most_expensive = max(products, key=products.get)
print(f"Самый дорогой: {most_expensive} - {products[most_expensive]} руб.")

# 7. Анализ имён
print("\n" + "=" * 40)
print("7. Анализ повторяющихся имён:")

names = ["Рамазан", "Кирилл", "Владимир", "Дмитрий", "Эдуард", "Рамазан", "Рамазан", "Владимир"]
print(f"Имена: {names}")
name_count = {}
for name in names:
    name_count[name] = name_count.get(name, 0) + 1
repeating = [name for name, count in name_count.items() if count > 1]
most_common = max(name_count, key=name_count.get)
print(f"Повторяющиеся имена: {repeating}")
print(f"Самое частое: '{most_common}' ({name_count[most_common]} раза)")

# 8. Первые вхождения символов
print("\n" + "=" * 40)
print("8. Первые вхождения символов:")

text = input("Введите строку: ")
first_occurrence = {}
for i, char in enumerate(text): #enumerate возвращает пары (индекс, символ)
    if char not in first_occurrence:
        first_occurrence[char] = i
print("Первые вхождения:")
for char, index in sorted(first_occurrence.items()):
    print(f"  '{char}': позиция {index}")