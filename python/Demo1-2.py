# nested Function

def outer():
    def inner():
        print("I am Inner")

    print("I am Outer")
    inner()

outer()
