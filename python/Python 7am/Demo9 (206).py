
a = 100 # Global Variable

def show():
    a = 199 # Local variable
    print(a)

print(a)
show()
print(a)