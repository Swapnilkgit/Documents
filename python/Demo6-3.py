
import re

s1 = "naveen is here"

result = re.match("naveen",s1)

if result:
    print("Match Found")
else:
    print("Match Not Found")
