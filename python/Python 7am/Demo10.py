
a = 100 # global variable

def display():
    global b # Global variable
    b = 99
    print(b)
    print(a+b)

print(a)
display()
print(a)
print(b)