user = "admin"
password = "1234"
user_input = input("Enter username : ")
user_password = input("Enter password : ")
if(user == user_input):
    if(password == user_password):
        print("Login Successful")
    else:
        print("Invalid Password")    
else:
    print("Invalid Username")