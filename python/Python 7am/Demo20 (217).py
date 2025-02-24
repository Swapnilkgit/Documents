
def details():
    idno = 101
    name = "Ravi"
    salary = 185000.00
    return idno,name,salary  # convert it into tuple (packing)


res = details()
print(res) # (101,"Ravi",185000.0)
