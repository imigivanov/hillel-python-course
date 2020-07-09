# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.


def cache(func):

    cache_dict = {}

    def helper(x):
        if cache_dict.get(x) is None:
            cache_dict[x] = func(x)
            helper.run_calls += 1
            result = "Function executed with counter = {}, function result = {}".format(helper.run_calls, cache_dict[x])
        else:
            helper.cache_calls += 1
            result = "Used cache with counter = {}, function result = {}".format(helper.cache_calls, cache_dict[x])

        return result

    helper.run_calls = 0
    helper.cache_calls = 0
    return helper


def divide_by_hundred(x):
    return x % 100

check_division = cache(divide_by_hundred)

print(check_division(50))
print(check_division(100))
print(check_division(5000))
print(check_division(100))