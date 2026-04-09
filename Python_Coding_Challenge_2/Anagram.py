str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()
anagram = sorted(str1) == sorted(str2)
print(anagram)