
department = {468:"CSE", 572:"ECE",621:"EEE",482:"Civil"}

did = int(input("Enter Department ID :"))

res = department.get(did,"Department is not Available")

print(res)