print("Hi there, this is a superuser gateway")
user = input("Username: ")
if user == "c4e":
    password = input("Password: ")
    if password == "codethechange":
        print("Welcome,",user)
    else:
        print("Password is incorrect")
else:
    print("You are not superuser!")