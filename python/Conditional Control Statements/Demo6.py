from firebase.firebase import FirebaseApplication
fb = FirebaseApplication("https://pythonwithnaveen-3b98f.firebaseio.com/")

print("Welcome to NNK Bank")
print("1) Create a New Account")
print("2) Bank Operations")
option = int(input("Select 1 Option from Menu : "))
if option == 1:
    result = fb.get("savingsaccount","")
    if result:
        x = result.keys() # Reading only keys (keys are account nos)
        key = list(x) # Converting into list
        accno = int(key[-1]) # reading last accno and converting into int
        accno = accno+1 # account no is incrimented so it is a new acc no
    else:
        accno = 1001
    name = input("Enter Account Holder Name : ")
    balane = float(input("Enter OPENING Balance : "))
    pin = int(input("Enter PIN No : "))
    fb.put("savingsaccount",accno,{"name":name,"balance":balane,"pino":pin})
    print("Account is Created")
elif option == 2:
    print("Bank Operations")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Check Balance")
    print("4) Transfer Amount")

else:
    print("Please Select from Given Options Only")
print("Thanks")