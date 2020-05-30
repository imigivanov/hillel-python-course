import functools


# def attribute_cache():
#     cache = {}
#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = my_func(args)
#         else:
#             return cache[args]
#
#     def clear_cache():
#         cache.clear()
#
#     return wrapper
#
# @attribute_cache
# def my_func():
#     """I am a doc string"""
#     print("My argument is {}".format(a))


# def capitilize_func(my_func):
#     def wrapper(args):
#         return args.upper()
#     return wrapper
#
# @capitilize_func
# def my_func(string):
#     return str(string)
#
# print(my_func("What does fox say?"))

def suppress_exception(err):
    def decorator(fn):

        def wrapper(*args):
            try:
                return fn(*args)
            except err as e:
                print("There is an error: {}".format(e.__doc__))

        return wrapper

    return decorator


@suppress_exception(KeyError)
def my_func(index):
    list_of_nothing = {}

    return list_of_nothing[index]


my_func(5)
