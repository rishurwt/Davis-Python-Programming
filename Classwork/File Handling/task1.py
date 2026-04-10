filev = open("first.txt","wt")
sentence = []
print('Enter Sentence : ')
for i in range(3):
    sentences = input()
    sentence.append(sentences + "\n")
    print('------------------')
filev.writelines(sentence)
print("Data Successfully written")
filev.close()
#To read the file
filev = open("first.txt","r")
print(filev.read())
filev.close()


