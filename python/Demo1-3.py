
from firebase.firebase import FirebaseApplication

fire = FirebaseApplication("https://pythonwithnaveen-9e89a.firebaseio.com/",None)

fire.post("Employee/101",{"name":"Ravi","salary":185000.00})

print("Data is saved")