# if else
# WAS to read 2 nos from user and print big no or same

no1 = int(input("Enter 1st No : "))
no2 = int(input("Enter 2nd No : "))

if no1 > no2:
    print(no1,"is Big NO")
else:
    if no2 > no1:
        print(no2, "is Big NO")
    else:
        print("both are same")
print("Thanks")