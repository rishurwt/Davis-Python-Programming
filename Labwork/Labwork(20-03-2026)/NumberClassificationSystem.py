def check_number(n):
    if n > 0:
        if n % 2 == 0:
            return "Positive and Even"
        else:
            return "Positive and Odd"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
numbers = [10, -5, 0, 7, -12]
for n in numbers:
    result = check_number(n)
    print(f"Number {n}: {result}")