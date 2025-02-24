
a = 100

def show():
    print(a) # name 'a' is used prior to global declaration
    global a
    a = 199
    print(a)

print(a)
show()
print(a)