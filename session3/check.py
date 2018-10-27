
s = input("nhap chu:")
if  (not s.islower()) and (not s.isupper()) and (not s.isdigit()):
    print("OK")
else:
    print("Not ok")