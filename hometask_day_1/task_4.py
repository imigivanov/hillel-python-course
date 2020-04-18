source_array = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

"""
4.1) Remove duplicates
"""


def output_result():
    print("Source array: {}".format(source_array))
    print("Array with removed duplicates: {}".format(no_duplicates_array))


# As we use Python 3.7, the simplest solution here is:
no_duplicates_array = list(dict.fromkeys(source_array))
output_result()

# Another way to do this is:
no_duplicates_array = []
for item in source_array:
    if item in no_duplicates_array:
        continue
    no_duplicates_array.append(item)

output_result()

"""
4.2) Print out 3 greatest numbers in the array:
"""

sorted_desc = no_duplicates_array  # in case I want to work with unmodified `no_duplicates_array` further in code
sorted_desc.sort(reverse=True)
print("Here are 3 of the largest numbers in the list: {}".format(sorted_desc[0:3]))

"""
4.3) Print out the index of a lesser value in the list.

Not sure here whether I supposed to print index of a lesser number from the source array 
or from the one without any duplicates, so I did both
"""


def lesser_num_index(provided_list):
    min_value_index = 0
    for index, value in enumerate(provided_list[1:]):
        if value <= provided_list[min_value_index]:
            min_value_index = index
    return min_value_index


print("The index of a lesser number from original array: {}".format(lesser_num_index(source_array)))
print(
    "The index of a lesser number from the array with no duplicates: {}".format(lesser_num_index(no_duplicates_array)))

"""
4.3) Output the source list in a reverse order
"""

print("The list in a reversed order: {}".format(list(reversed(source_array))))