# Task 1

# my_string = str(input("Enter the string:\n"))
# change_character = my_string[0].lower()
# new_string = my_string[0] + my_string[1:].lower().replace(change_character, "$")
# print(new_string)

# Task 2

"""
2) Add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged. 
"""

my_string = str(input("Enter the string:\n"))

if len(my_string) < 3:
    print(my_string)
    exit(0)

if my_string[-3:].find("ing") >= 0:
    print(my_string + "ly")
    exit(0)

print(my_string + "ing")