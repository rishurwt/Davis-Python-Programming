text = input("Enter text: ")
duplicates = []
for char in text:
    if text.count(char) > 1 and char not in duplicates:
        duplicates.append(char)
print(f"Output: {' '.join(duplicates)}")