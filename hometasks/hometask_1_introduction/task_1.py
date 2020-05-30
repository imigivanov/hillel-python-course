my_dictionary = {}

for i in range(1, 11):
    my_dictionary[i] = i * i
print(my_dictionary)

# Or with checking whether the provided key already exists:
for i in range(1, 11):
    if i not in my_dictionary.keys():
        my_dictionary[i] = i * i
print(my_dictionary)

# Or just using dictionary comprehensions described in PEP 274
print({i: i * i for i in range(1, 11)})
