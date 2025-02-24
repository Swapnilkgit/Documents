print("Hi")
def one():
    print("One")

def two():
    print("Two")
    one()

def three():
    two()
    print("Three")

three()
one()
two()
print("Bye")