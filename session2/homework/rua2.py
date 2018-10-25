from turtle import *
shape("turtle")
speed(0)


for i in range(3,7):
    if i%2==0:
        color('red')
    else:
        color('blue')
    for o in range(i):
        forward(100)
        left(360/i)

mainloop()
