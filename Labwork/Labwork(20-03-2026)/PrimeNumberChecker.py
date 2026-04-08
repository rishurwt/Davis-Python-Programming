def is_prime(num):
    if num < 2:
        return False 
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False 
    return True 
n = int(input("Enter a number "))
if is_prime(n):
    print(f"{n} ek Prime Number hai!")
else:
    print(f"{n} Prime Number nahi hai.")