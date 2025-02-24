
def outer(fun):
    def inner():
        fun()
        print("Good Morning")
    return inner

def wish():
    print("Hello World")

def display():
    print("Hello Students")


inn = outer(display)
inn()
