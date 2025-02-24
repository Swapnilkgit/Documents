# In python If mutliple variables are holding same value will reff to one object.

a = 100
b = 200
c = 100
print(a,b,c)
print(a,b,c,sep="-")
print(id(a))
print(id(b))
print(id(c))

print("-------------------------------------")

# In python Every thing is an object model only.(class,function,variable)
# In python we can declare Mutiple variables in 1 line.

a,b,c = 10,20,30
print(a,b,c)

idno,name,salary,status = 101,"Ravi",185000.00,True
print(idno,salary,name,status,sep="-----")

print("-------------------------------------")

# In python 1 varialbe can hold Mutiple values.

employee_details = 101,"Ravi",185000.00,True  # In python we call it as "packing"
# BY default the python will convert it into "tuple" type.

print(employee_details)
print(type(employee_details))

# un-packing example

idno,name,salary,status = employee_details
print(idno)
print(name)
print(salary)
print(status)









