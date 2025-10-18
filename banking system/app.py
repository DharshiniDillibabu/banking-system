balance=5000
while True:
    user=input("enter pin:")
    if user!="1234":
        print("incorrect pin")
        continue
    print(f"Current balance: ${balance}")
    action = input("Would you like to deposit(d), withdraw(w),checkbalance(c) or exit?(e) ").strip().lower()
    
    if action == "d":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited.")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif action == "w":
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn.")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")
    elif action =="c":
        print(f"Your current balance is: ${balance}")
    
    elif action == "e":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid action. Please choose deposit, withdraw, or exit.")

    #exit()
