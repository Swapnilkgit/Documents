def pin(fun):
    def inner():
        pin = int(input("Enter Pin No :"))
        if pin == 5475:
            fun(int(input("Enter Amount :")))
        else:
            print("Invalid Pin")
    return inner

@pin
def withdraw(amount):
    print("Withdraw Amount is :",amount)


withdraw()