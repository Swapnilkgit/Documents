
def outer(no):
    def inner():
        print(no)

    return inner


inn = outer(1000)
del outer
inn()