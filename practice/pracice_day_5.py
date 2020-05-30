def newline_space_formatter(filename):
    with open(filename, "r") as w:
        string_to_format = w.read()
    return string_to_format.replace("\n", "").replace(" ", "")


print(newline_space_formatter("foo.txt"))