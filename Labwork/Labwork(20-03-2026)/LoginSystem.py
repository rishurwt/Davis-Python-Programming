def login():
    username = "admin"
    password = "1234"
    attempts = 0 
    while attempts < 3:
        u_input = input("Enter Username: ")
        p_input = input("Enter Password: ")

        if u_input == username and p_input == password:
            print("Login Successful!")
            return
        attempts += 1 # Ek galat attempt
        print(f"Wrong credentials. Attempts left: {3 - attempts}")
    print("Account Locked!")
login()