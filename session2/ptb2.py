print("ax^2+bx+c=0")
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
delta=b*b-(4*a*c)
if delta>0:
    print("pt co 2 nghiem phan biet")
    x1=((-b)+(delta**0.5))/(2*a)
    x2=((-b)-(delta**0.5))/(2*a)
    print("x1=",x1,"x2=",x2)
elif delta==0:
    print("pt co nghiem duy nhat")
    x=-b/(2*a)
    print("x=",x)
else:
    print("pt vo nghiem")