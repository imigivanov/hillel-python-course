my_list = []

for i in range(100):
    if i % 2 == 0:
        my_list.append(i)

print(my_list)

# Or using list comprehensions described in PEP 202
print([i for i in range(100) if i % 2 == 0])