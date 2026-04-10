filev = open("first.txt","w+")
sentence = []
print('Enter Sentence : ')
for i in range(2):
    sentences = input()
    sentence.append(sentences + "\n")
    print('------------------')
filev.writelines(sentence)
print("Data Successfully written")
# filev.close()
filev.seek(0)

#To read the file

# filev = open("first.txt","r")
print(filev.read())
filev.close()


