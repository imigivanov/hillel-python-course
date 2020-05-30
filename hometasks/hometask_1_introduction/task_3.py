import random

my_random_string = list("This is just a random string here.")
vowels_upper = "AEIOUY"
vowels_lower = "aeiouy"
consonants_upper = "BCDFGHJKLMNPQRSTVWXZ"
consonants_lower = "bcdfghjklmnpqrstvwxz"

for i, value in enumerate(my_random_string):

    if value.islower():
        consonants = consonants_lower
        vowels = vowels_lower
    elif value.isupper():
        consonants = consonants_upper
        vowels = vowels_upper
    else:
        continue

    index = consonants.find(value)

    if index < 0:
        continue

    if index >= len(vowels):
        index = random.randint(0, len(vowels) - 1)

    my_random_string[i] = vowels[index]

final_str = ''.join(my_random_string)

print(final_str)
