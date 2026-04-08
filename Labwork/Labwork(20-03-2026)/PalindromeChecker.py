def is_palindrome(data):
    original = str(data).lower()
    reversed_data = ""
    for char in original:
        reversed_data = char + reversed_data
    if original == reversed_data:
        return True
    else:
        return False
user_input = input("Enter any input ")

if is_palindrome(user_input):
    print(f"Haan! '{user_input}'  Palindrome hai.")
else:
    print(f"Nahi! '{user_input}' Palindrome nahi hai.")