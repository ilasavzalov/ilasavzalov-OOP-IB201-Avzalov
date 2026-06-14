def check_password(required_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Введите пароль: ")
            if password == required_password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None
        return wrapper
    return decorator

@check_password('password')
def make_burger(type_of_meat, with_onion=False, with_tomato=True):
    print('Булочка')
    if with_onion:
        print('Луковые колечки')
    if with_tomato:
        print('Ломтик помидора')
    print('Котлета из', type_of_meat)
    print('Булочка')


make_burger('говядины', with_onion=True, with_tomato=True)
# Ввод: admin123 -> Вывод:
# Булочка
# Луковые колечки
# Ломтик помидора
# Котлета из говядины
# Булочка

# Пример с разными паролями для разных функций
@check_password('password')
def secret_info():
    return "Секретная информация"

@check_password('open123')
def public_info():
    return "Общедоступная информация"

# Каждая функция требует свой пароль
