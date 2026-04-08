tuple = (5,1,8,2)
max = -10
min = 1000
for i in range(0,4):
    if(max < tuple[i]):
        max = tuple[i]
    if(min > tuple[i]):
        min = tuple[i]
print("Minimum is ",min," Maximun is ",max)     
