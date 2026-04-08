def print_pattern(rows):
    for i in range(1, rows + 1):
        if i % 2 == 0:
            char = "*"
        else:
            char = "#"
        print((char + " ") * i)
print_pattern(5)