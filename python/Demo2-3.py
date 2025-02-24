
from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://pythonwithnaveen-9e89a.firebaseio.com/",None)

fire.put("Employee",103,{"name":"Mohan","salary":125000.00})

print("Data is saved")

