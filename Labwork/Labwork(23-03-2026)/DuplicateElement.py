list = [1,2,3,2,4,5,1]
duplist = []
for i in range(0,7):
    for j in range(i+1,7):
        if(list[i]==list[j]):
            duplist.append(list[i])

print(duplist)