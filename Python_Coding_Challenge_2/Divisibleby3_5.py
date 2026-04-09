payment = int(input("Enter Payment Amount : "))
if(payment%5==0):
    if(payment%3==0):
        print("Yes")
    else:
        print("No")
else:
    print("No")    