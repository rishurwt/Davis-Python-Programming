filev = open("first.txt","wt")
sentence = []
print('Enter Sentence : ')
for i in range(5):
    sentences = input()
    sentence.append(sentences)
    
    print('------------')
filev.writelines(sentence)
print("Data Successfully written")

filev.close()

filev = open("first.txt","r")
print(filev.read())
filev.close()


