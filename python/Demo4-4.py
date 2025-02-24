

from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://pythonwithnaveen-9e89a.firebaseio.com/",None)

# Deleting 1 Record
#fire.delete("Employee",103)
#print("Deleted")

# Deleting all the Records
fire.delete("Employee",None)
print("Deleted")

