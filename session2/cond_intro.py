yob = int(input("Nam sinh cua ban: "))
age = 2018 -yob
print(age)
if age<10:
    print("Children")
elif age < 18:
    print("teenager")
else:
    print("Adult")