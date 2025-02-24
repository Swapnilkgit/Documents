def outer(fun):
    def inner():
        fun()
        print("Good Morning")
    return inner

@outer
def wish():
    print("Hello World")

@outer
def display():
    print("Hello Students")

wish()
display()