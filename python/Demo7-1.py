import copy as cp

nos = {10,20,30}
val = cp.copy(nos)

print(nos) # [10,20,30]
print(val) # [10,20,30]

nos.add(99)

print(nos) # [10,99,30]
print(val) # [10,20,30]