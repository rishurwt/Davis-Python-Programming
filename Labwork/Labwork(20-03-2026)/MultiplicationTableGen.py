def generate_table(n):   
    if n < 0:
        print("Please enter a positive number!!")
    else:
        print(f"--- Table of {n} ---")
        for i in range(1, 11):
            result = n * i
            print(f"{n} x {i} = {result}")
num = int(input("Enter a number to get its table: "))
generate_table(num)