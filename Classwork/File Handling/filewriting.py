filev = open("first.txt","w")
print('Enter Sentence : ')
for i in range(5):
    sentence = input()
    filev.write(sentence)
    print('------------')
print("Data Successfully written")
filev.close()
# print(filev.read)