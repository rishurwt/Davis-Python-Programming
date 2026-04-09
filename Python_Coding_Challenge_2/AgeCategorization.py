age = int(input("Enter your age : "))
if(age<0) :
    print("Enter Valid age")
elif(age<18):
    print("Minor")
elif(age<50):
    print("Adult")
elif(age<120):
    print("Senior ")
else:
    print("Enter Valid age")
