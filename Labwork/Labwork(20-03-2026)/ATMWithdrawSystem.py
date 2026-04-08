def atm_system():
    balance = 10000  
    
    while True:
        print("\n--- Welcome to ATM ---")
        print(f"Current Balance: {balance}")
        print("1. Withdraw Money")
        print("2. Exit")
        
        choice = input("Select Option (1/2): ")
        
        if choice == "1":
            amount = int(input("Enter amount to withdraw : "))
            if amount < 0:
                print("Error: Invalid amount! ")
            elif amount > balance:
                print("Error: Insufficient balance! ")
            else:
                balance -= amount 
                print(f"Withdraw Success! {amount} ")
                print(f"Naya Balance: {balance}")
                
        elif choice == "2":
            print("Thank you for using our ATM.")
            break  
        else:
            print("Invalid Choice! Please select 1 ya 2 ")
atm_system()