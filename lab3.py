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

#Задание 4 собственный итератор 
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result
    

for x in Countdown(5):
    print(x)

#Задание 5 собственный генератор Фибоначчи
def fibonacci(n):
    if n <= 0:
        return
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print('\nПервые n чисел Фибоначчи')
for num in fibonacci(5):
    print(num)
