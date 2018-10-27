item =["T-Shirt","Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
while True:

    if (n == "r") or (n=="R"):
        print(*item,sep=", ")
        n = input("Welcome to our shop, what do you want (C, R, U, D)? Ctrl+C to exit")

    elif (n == "c")or (n== "C"):
        new = input("Enter new item: ")
        item.append(new)
        print("our items: ", end='')
        print(*item, sep=", ")
        n = input("Welcome to our shop, what do you want (C, R, U, D)? Ctrl+C to exit")

    elif (n == "u")or(n=="U"):
        print(*item, sep=", ")
        i = int(input("Update position? "))
        while i > len(item):
            print("not in range")
            i = int(input("Update position? "))
        update = input("Thay the thanh: ")
        item[i-1] = update
        print("our items: ", end='')
        print(*item, sep=', ')
        n = input("Welcome to our shop, what do you want (C, R, U, D)? Ctrl+C to exit")

    elif (n == "d")or(n == "D"):
        print(*item, sep=", ")
        d = int(input("Delete position? "))
        while d > len(item):
            print("not in range")
            d = int(input("Update position? "))
        item.pop(d-1)
        print("our items: ", end='')
        print(*item, sep=', ')
        n = input("Welcome to our shop, what do you want (C, R, U, D)? Ctrl+C to exit")
    else:
        print("You must choose C, R, U, D")
        n = input("Welcome to our shop, what do you want (C, R, U, D)? Ctrl+C to exit")
