

from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://pythonwithnaveen-9e89a.firebaseio.com/",None)

# Reading all records
#result = fire.get("Employee",None)
#print(result)

# Read 1 record
idno = int(input("Enter IDNO :"))
res = fire.get("Employee",idno)
if res:
    print(res)
else:
    print("Invalid IDNO")

