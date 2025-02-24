# Example on Default arguments

def add(no1=10,no2=0):
    print(no1)
    print(no2)
    print(no1+no2)

add()
print("---------")
add(100)
print("---------")
add(100,20)
print("---------")
add(no2=1000) # keyword
print("---------")
add(no2=90,no1=-50)