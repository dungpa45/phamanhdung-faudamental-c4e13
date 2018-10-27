print("Hi there, this is a superuser gateway")
user = input("Username: ")
while True:
    if user == "c4e":
        password = input("Password: ")
        while True:
            if password == "codethechange":
                print("Welcome,", user)
                break
            else:
                print("Password is incorrect")
            password = input("Password: ")
        break
    else:
        print("You are not superuser!")
    user = input("Username: ")
