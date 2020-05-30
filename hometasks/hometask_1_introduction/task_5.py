dict_one = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
dict_two = { 'a': 6, 'b': 7, 'z': 20, 'x': 40 }
common_keys = []

for i in dict_one.keys():
    if i in dict_two.keys():
        common_keys.append(i)

print("Common keys are: {}".format(common_keys))