# shallow copy will not work with nested list

import copy as cp

nos = [[10,20],[30,40]]
val = cp.copy(nos)

print(nos) # [[10,20],[30,40]]
print(val) # [[10,20],[30,40]]

nos[1][0] = 99

print(nos) # [[10,20],[99,40]]
print(val) # [[10,20],[99,40]]
