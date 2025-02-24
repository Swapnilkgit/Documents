
def outer():
    a = 1000
    def inner():
        nonlocal a
        a = 5000
        print(a)
    print(a)
    inner()
    print(a)


outer()