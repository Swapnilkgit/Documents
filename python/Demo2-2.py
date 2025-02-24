
def outer():
    a = 100
    def inner():
        print(a)

    print(a)
    inner()

outer()

