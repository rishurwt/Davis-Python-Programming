list = [10, 20, 30, 40, 50]
k = 2
for i in range(k):
    le  = list.pop()
    list.insert(0,le)
print(list)    