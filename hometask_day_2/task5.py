my_string = "hello 1 one two three 15 world"

def find_three_words_in_a_row(string):
    str_to_search = string.split()
    counter = 0
    for word in str_to_search:

        if counter == 3:
            return "There are 3 words in a row"

        try:
            num = int(word)
            counter = 0
        except ValueError:
            counter += 1
            continue

    return "There are no 3 words in a row"

print(find_three_words_in_a_row(my_string))