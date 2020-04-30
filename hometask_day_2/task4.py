def power_of_num(array, n):

    print(array)
    print(array[n])
    print(n)

    if len(array) <= n:
        return -1

    if n == 0:
        return 1

    power = 1

    for i in range(1, n):
        power *= my_arr[n]

    return power

my_arr = [2, 3, 5, 7, 3, 0]

n = int(input("Input the index of number you would like to find power of:\n"))

print(power_of_num(my_arr, n))