text = input("Enter text: ")
vowels = "aeiouAEIOU"
for char in vowels:
    text = text.replace(char, "*")
print("Masked text is ",text)
