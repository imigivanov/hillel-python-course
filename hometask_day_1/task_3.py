my_random_string = list("This is just a random string here.")
my_new_random_string = ""
vowels = "AEIOUYaeiouy"
consonants = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"
for i in range(len(my_random_string)):
    for j in range(len(vowels)):
        if my_random_string[i] in vowels[j]:
            print(my_random_string[i])
            my_random_string[i] = consonants[j]
    my_new_random_string += my_random_string[i]

print(my_new_random_string)