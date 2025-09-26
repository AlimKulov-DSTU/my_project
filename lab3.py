#Задание 1 список квадратов чисел
squares = [x**2 for x in range(1, 11)]
print(squares)

#Задание 2 фильтрация четные числа
list_filtered = [x for x in range(1, 20) if x % 2 == 0]
print(list_filtered)

#Задание 3 работа со строками 
words = ['python', 'Java', 'c++', 'Rust', 'go']
words_new = [word.upper() for word in words if len(word) > 3]
print(words_new)
