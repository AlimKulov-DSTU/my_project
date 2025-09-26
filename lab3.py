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

#Задание 6 калькулятор Decimal калькулятор
from decimal import Decimal, getcontext

getcontext().prec = 10

def calculate_deposit(RUB, STV, t):
    RUB = Decimal(str(RUB))
    STV = Decimal(str(STV))
    t = Decimal(str(t))
    
    F = RUB * (1 + (STV / (12 * 100))) ** (12 * t) #Формула
    
    F = F.quantize(Decimal('0.01')) #Округление до 2 знаков после запятой (копейки)
    
    profit = F - RUB
    
    return F, profit

RUB = 1000.00  # Начальная сумма
STV = 7.5      # Процентная ставка
t = 2        # Срок

S, profit = calculate_deposit(RUB, STV, t)

print(f"\nИтоговая сумма: {S:.2f} руб.")
print(f"Прибыль: {profit:.2f} руб.")

#Задание 7 Fraction (рациональные дроби)
from fractions import Fraction

x = Fraction('3/4')
y = Fraction('5/6')

print(f"\nДробь 1: {x} (десятичная форма: {float(x):.2f})")
print(f"Дробь 2: {y} (десятичная форма: {float(y):.2f})")
print(f"Сложение: {x + y} (десятичная форма: {float(x + y):.2f})")
print(f"Вычитание: {x - y} (десятичная форма: {float(x - y):.2f})")
print(f"Умножение: {x * y} (десятичная форма: {float(x * y):.2f})")
print(f"Деление: {x / y} (десятичная форма: {float(x / y):.2f})")

#Задание 8 Datetime вывод
from datetime import datetime, date, time

date = datetime.now()

print("\n", datetime.now())
print(date.date())
print(date.time())

#Задание 9 Date Time (разница дат)
birthday = datetime(2004, 4, 8)
now = datetime(2025, 9, 26)

next_birthday = datetime(now.year, birthday.month, birthday.day)

if now > next_birthday:
    next_birthday = datetime(now.year + 1, birthday.month, birthday.day)

days_until_birthday = (next_birthday - now).days

print (f'\nРазница между датой рождения и заданной {now - birthday}')
print(f"Дней до дня рождения: {days_until_birthday} дней")
