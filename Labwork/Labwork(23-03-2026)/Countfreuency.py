tuple = (1, 2, 2, 3, 1, 4)
frequency = {}
for item in tuple:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(frequency)

