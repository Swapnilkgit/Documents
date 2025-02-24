
# WAS to read 2 nos from user and print big no or same

no1 = int(input("Enter 1st No : "))
no2 = int(input("Enter 2nd No : "))

if no1 > no2:
    print(no1,"is BIG No")
if no2 > no1:
    print(no2,"is BIG No")
if no1 == no2:
    print("Both are same")
print("Thanks")