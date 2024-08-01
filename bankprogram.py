def show_balance(balance):
    print(".........................................")
    print(f"Your balance is RM{balance:.2f}")
    
    

def deposit():
    print(".........................................")
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount < 0:
        
        print("That's not a valid amount")
        print(".........................................")
        
        return 0  
    else:
        return amount
    

def withdrawal(balance):
    print(".........................................")
    amount = float(input("Enter an amount to be withdrawn: "))
    
    
    if amount > balance:
        print(".........................................")
        print("You have insufficient funds")
        
        return 0
    elif amount < 0:
        print(".........................................")
        print("Amount must not be less than 0")
        
        return 0
    else:
        return amount


def main():

    balance=0
    is_running = True

    while is_running:
        print(".........................................")
        print("Bank Program")
        print("1.Check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print(".........................................")
        choice= input("Enter your choice (1-4):")
        

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdrawal(balance)
        elif choice == "4":
            is_running = False
        else:
            print(".........................................")
            print("That is an invalid choice")
            
    print(".........................................")
    print("Thank you!! Have a nice day!")
    print(".........................................")
    

if __name__=='__main__':
    main()