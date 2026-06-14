def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == "secret":
            return func(*args, **kwargs)
        else:
            print("В доступе отказано")
            return None
    return wrapper

@check_password
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
