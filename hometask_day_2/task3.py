# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

num = input("Please input the number:\n")

def mult_num(num):
    mult = 1
    for i in num:
        if int(i) != 0:
            mult *= int(i)
    return mult

print(mult_num(num))