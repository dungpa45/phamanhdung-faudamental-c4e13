yob_str = input("Nhap nam sinh: ")
while not yob_str.isdigit():
    print("Nhap so di")
    yob_str = input("Nhap nam sinh: ")

yob = int(yob_str)
age =2018 -yob
print("Tuoi la:",age)
