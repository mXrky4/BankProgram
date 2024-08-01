def show_balance():
    print(".........................................")
    print(f"Your balance is RM{balance}")
    pass

def deposit():
    print(".........................................")
    pass

def withdrawal():
    print(".........................................")
    pass

balance=0
is_running = True

while is_running:
    print("Bank Program")
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice= input("Enter your choice (1-4):")

    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdrawal()
    elif choice == "4":
        is_running = False
    else:
        print("That is an invalid choice")
        print(".........................................")
print(".........................................")
print("Thank you!! Have a nice day!")