# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.

def division_wrapper(func):
    def wrapper(x):
        result = func(x)
        if result == 0:
            return "We are OK!"
        else:
            return "Bad news guys, we got {}".format(result)

    return wrapper


def divide_by_hundred(x):
    return x % 100

check_division = division_wrapper(divide_by_hundred)

print(check_division(50))
