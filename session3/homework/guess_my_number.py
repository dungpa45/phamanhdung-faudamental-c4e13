import random
rnd=random.randrange(1,100)
n = int(input("guess my number? (1-100) "))
while n!=rnd:
    if rnd < n:
        print("A little too large")
        n = int(input("guess my number? (1-100) "))
    elif rnd >n:
        print("A little too small")
        n = int(input("guess my number? (1-100) "))
    print("Bingo")