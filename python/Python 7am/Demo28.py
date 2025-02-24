nos = []
def add():
    no1 = int(input("Enter 1st No :"))
    no2 = int(input("Enter 2ns No :"))
    nos.append(no1+no2)

for x in range(5):
    add()
print(nos)

x = int(input("Enter a No :"))
print(x in nos)

