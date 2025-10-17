# Декоратор логирования
def logger(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"Вызов функции {func_name} с аргументами {signature}")
        
        result = func(*args, **kwargs)
        
        print(f"Функция {func_name} вернула {result}")
        
        return result
    return wrapper

# Функции с применением декоратора логирования
@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

@logger
def greet(name):
    greeting = f"Привет, {name}!"
    print(greeting)
    return greeting

# Декоратор доступа
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            user_role = user.get('role', 'guest')
            user_name = user.get('name', 'Unknown')
            
            if user_role in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user_name}")
                return None
        return wrapper
    return decorator

# Функции с ограничением доступа
@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return True

@require_role(["admin", "publisher"])
def publish_content(user):
    print(f"Контент опубликован пользователем {user['name']}")
    return True

# Тестирование
def main():
    print("Тестирование декоратора логирования")
    add(5, 3)
    divide(10, 2)
    divide(10, 0)
    greet("Kirill")

    print("\nТестирование декоратора доступа")
    # Создаем пользователей
    admin = {'name': 'Kirill', 'role': 'admin'}
    publisher = {'name': 'Dmitriy', 'role': 'publisher'}
    guest = {'name': 'User Name', 'role': 'guest'}

    # Тестируем доступ к удалению базы данных
    print("\nПроверка удаления базы данных:")
    delete_database(admin)
    delete_database(publisher)
    delete_database(guest)

    # Тестируем доступ к публикации контента
    print("\nПроверка публикации контента:")
    publish_content(admin)
    publish_content(publisher)
    publish_content(guest)

if __name__ == "__main__":
    main()