string = input("Enter a string ").strip()
if(string == string[: :-1]):
    print("Palindrome")
else:
    print("not palindrome")