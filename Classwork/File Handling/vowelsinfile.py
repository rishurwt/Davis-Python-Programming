filev = open("first.txt","r")
vowels = "aeiouAEIOU"
data = filev.read()
vowel_count = 0

if(len(data)>0):
    for char in data:
        if char in vowels:
            vowel_count = vowel_count + 1
print("Total nmber of vowel is ",vowel_count)
