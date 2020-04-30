def most_frequent(list_var):
    return max(set(list_var), key=list_var.count)


def most_frequent_var2(list_var):
    counter = 0  # this will count how many times the element we're checking appears in the list
    most_freq_elem = list_var[0]  # we can basically assign most freq. elem. by default as the first one before further
    # processing

    for elem in list_var:
        freq = list_var.count(elem) # let's check how many times does this element appears in our list
        if (freq > counter):
            counter = freq
            most_freq_elem = elem

    return most_freq_elem

my_list = (['a', 'a', 'bi', 'bi', 'bi'])

print(most_frequent(my_list))
print(most_frequent_var2(my_list))
