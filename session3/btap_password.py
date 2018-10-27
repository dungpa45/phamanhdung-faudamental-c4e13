p = input("Nhap password: ")
while True:
    print("not ok")
    if len(p)<=8:
        print("Nhap pass >8 ky tu")
    elif p.isalpha():
        print("pass phai co chu")
    elif p.islower() or p.isupper() or p.isdigit():
        print("pass phai co chu hoa va thuong va so")
    else:
        break
    p = input("Nhap password: ")

print("done")
