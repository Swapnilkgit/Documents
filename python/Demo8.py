for x in range(3):
    pno = int(input("Enter PIN No : "))
    if pno == 5475:
        print("Welcome User")
        break
    else:
        print("Wrong PIN Number")
        ans = int(input("To continue press 1 "))
        if ans == 1:
            continue
        else:
            break
else:
    print("Sorry Your Account is Blocked ")
    print("Please Do Contact the home branch")

print("Thanks")
