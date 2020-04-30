def power_of_num(array, n):

    if len(array) <= n:
        return -1

    return array[n] ** n

my_arr = [2, 3, 5, 7, 3, 0]

n = int(input("Input the index of number you would like to find power of:\n"))

print(power_of_num(my_arr, n))