import re

def validate_login(login):
    if not login:
        return False
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{3,18}[a-zA-Z0-9]$'
    
    return bool(re.match(pattern, login))

def find_dates(text):
    pattern = r'\b(\d{1,2})[.-/](\d{1,2})[.-/](\d{2}|\d{4})\b'
    matches = re.findall(pattern, text)
    dates = []
    for d, m, y in matches:
        day = d.zfill(2)
        month = m.zfill(2)
        year = y if len(y) == 4 else f'20{y}' if int(y) <= 99 else y
        dates.append(f"{day}.{month}.{year}")
    return dates

import re

def parse_log(log_line):
    ipv4 = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    ipv6 = r'(?:(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|' \
           r'(?:[0-9a-fA-F]{1,4}:){6}(?::[0-9a-fA-F]{1,4}|:(?::[0-9a-fA-F]{1,4}){1,5})|' \
           r'(?:[0-9a-fA-F]{1,4}:){5}(?:(?::[0-9a-fA-F]{1,4}){1,2}|:(?::[0-9a-fA-F]{1,4}){1,4})|' \
           r'(?:[0-9a-fA-F]{1,4}:){4}(?:(?::[0-9a-fA-F]{1,4}){1,3}|:(?::[0-9a-fA-F]{1,4}){1,3})|' \
           r'(?:[0-9a-fA-F]{1,4}:){3}(?:(?::[0-9a-fA-F]{1,4}){1,4}|:(?::[0-9a-fA-F]{1,4}){1,2})|' \
           r'(?:[0-9a-fA-F]{1,4}:){2}(?:(?::[0-9a-fA-F]{1,4}){1,5}|:(?::[0-9a-fA-F]{1,4}){1})|' \
           r'(?:[0-9a-fA-F]{1,4}:){1}(?:(?::[0-9a-fA-F]{1,4}){1,6}|:(?::[0-9a-fA-F]{1,4}){0,1})|' \
           r'(?::(?:(?::[0-9a-fA-F]{1,4}){1,7}|(?::[0-9a-fA-F]{1,4}){0,1}))|' \
           r'(?:(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4})?)'

    pattern = (
        r'^(\d{4}-\d{2}-\d{2}) '
        r'(\d{2}:\d{2}:\d{2}) '
        r'\w+ '
        r'user=(\S+) '
        r'action=(\S+) '
        r'ip=(' + ipv4 + r'|' + ipv6 + r')'
        r'$'
    )

    match = re.match(pattern, log_line.strip())
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'user': match.group(3),
            'action': match.group(4),
            'ip': match.group(5)
        }
    return None

def validate_password(password):
    if len(password) < 8:
        return False
    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).+$'
    return bool(re.match(pattern, password))

def validate_email_domain(email, domains):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False
    domain = email.split('@')[-1].lower()
    return domain in [d.lower() for d in domains]

import re

import re

def normalize_phone(phone):
    #Удаляем всё кроме цифр
    digits = re.sub(r'\D', '', phone)
    
    if not digits:
        return ''
    
    #Если 11 цифр и начинается с 8 — заменяем первую 8 на 7
    if len(digits) == 11:
        digits = re.sub(r'^8', '7', digits)
    
    #Если 10 цифр — добавляем 7 спереди
    elif len(digits) == 10:
        digits = re.sub(r'^', '7', digits)  # ^ — начало строки, так добавляем префикс
    
    #Для других длин — считаем некорректным
    else:
        return ''
    
    #Финальная проверка: ровно 11 цифр, начинается с 7
    if re.fullmatch(r'^7\d{10}$', digits):
        return '+' + digits
    
    return ''


print("Задание 1. Валидация логина")
login = input("Логин: ").strip()
print("Результат:", "валидный" if validate_login(login) else "невалидный")
print()

print("Задание 2. Поиск дат")
text = input("Текст: ").strip()
dates = find_dates(text)
print("Найденные даты:", ", ".join(dates) if dates else "не найдено")
print()

print("Задание 3. Парсинг лога")
log_line = input("Строка лога: ").strip()
log_data = parse_log(log_line)
print("Результат:", log_data if log_data else "не распознан")
print()

print("Задание 4. Проверка пароля")
password = input("Пароль: ").strip()
print("Результат:", "подходит" if validate_password(password) else "не подходит")
print()


ALLOWED_DOMAINS = ['gmail.com', 'yandex.ru', 'mail.ru', 'edu.ru', 'outlook.com']
print("Задание 5. Проверка email (допустимые домены:", ", ".join(ALLOWED_DOMAINS), ")")
email = input("Email: ").strip()
print("Результат:", "подходит" if validate_email_domain(email, ALLOWED_DOMAINS) else "не подходит")
print()

print("Задание 6. Нормализация телефона")
phone = input("Номер телефона: ").strip()
normalized = normalize_phone(phone)
print("Нормализованный номер:", normalized)