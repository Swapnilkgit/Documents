# 123
# 123
# 123

for x in range(3):
    print(123)
print("--------------------")
print("123\n"*3)
print("--------------------")

# 123
# 123
# 123

for x in range(3):
    for y in range(3):
        print(y+1,end="")
    print()

print("--------------------")

# 111
# 222
# 333

for x in range(3):
    for y in range(3):
        print(x+1,end="")
    print()

print("--------------------")

# 123
# 456
# 789

counter = 1
for x in range(3):
    for y in range(3):
        print(counter,end="")
        counter+=1
    print()

print("-----------------------------")

# ABC
# DEF
# GHI

counter = 65
for x in range(3):
    for y in range(3):
        print(chr(counter),end="")
        counter+=1
    print()

print("-----------------------------")

# A*C
# D*F
# G*I

counter = 65
for x in range(3):
    for y in range(3):
        if y == 1:
            print("*",end="")
        else:
            print(chr(counter),end="")
        counter+=1
    print()


print("-----------------------------")

# A*C
# D*F
# G*I

counter = 65
for x in range(3):
    for y in range(3):
        if y == 1:
            print("*",end="")
        else:
            print(chr(counter),end="")
        counter+=1
    print()


