# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

def checking_type(func):
    def wrapper(x):
        if isinstance(x, int):
            return func(x)
        elif isinstance(x, str):
            raise ValueError("string type is not supported")
        else:
            raise ValueError("provided type is not supported")

    return wrapper

def add_hundred(x):
    return x + 100

solution = checking_type(add_hundred)

print(solution(10))