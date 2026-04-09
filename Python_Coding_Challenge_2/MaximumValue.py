list = []
size = int(input("Enter total number of element : "))
for i in range(size):
    num = int(input(f"Enter {i+1} element "))
    list.append(num)
max = list[0]
for i in list:
    if(i> max):
        max = i   
print("Max value is ",max) 
