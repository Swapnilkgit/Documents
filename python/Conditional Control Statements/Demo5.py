
balance = 500
pin = int(input("Enter PIN No : "))

if pin == 5475:
    amount = int(input("Enter amount to Withdraw : "))
    if amount%100 == 0:
        if amount <= 10000:
            if amount <= balance:
                balance = balance - amount
                print("Withdraw amount is ",amount)
                print("Current Balance = ",balance)
            else:
                print("No Funds")
        else:
            print("Max withdraw Amount is 10000/-")
    else:
        print("Invalid Amount")
else:
    print("Invalid Pin No")

print("Thanks")