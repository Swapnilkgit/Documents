a = 100 # global variable

def display():
    global b # Global variable
    b = 99
    print(b)
    c = a+b
    print(c)

print(a)
display()
print(a)
print(b)
print(c)