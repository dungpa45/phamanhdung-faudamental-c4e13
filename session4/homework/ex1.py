# 2.1
size_sheep = [5,7,300,90,24,50,75]
print("Hello, These are my sheep sizes")
print(size_sheep)
print("==========================================================")

# 2.2
s_max = max(size_sheep)
print("Now my biggest sheep size",s_max,"let's shear it")
print("==========================================================")

#2.3
print("After shearing , here is my flock")
s=size_sheep.index(s_max)
size_sheep[s]=8
print(size_sheep)
print("==========================================================")

#2.4
print("1 month has passed, now here is my flock")

# for i in size_sheep:
#     a = size_sheep.index(i)
#     size_sheep[a]+=50
# print(size_sheep)
print("==========================================================")

#2.5

for month in range(1,4):
    print("MONTH",month)
    print("1 month has passed, now here is my flock")
    for i in size_sheep:
        a = size_sheep.index(i)
        size_sheep[a] += 50
    print(size_sheep)
    s_max = max(size_sheep)
    if month == 3:
        tong = sum(size_sheep)
        tien = tong*2
        print("My flock has size in total : ", tong)
        print("I would get ", tong, " *2$ = ", tien, "$")
    print("Now my biggest sheep size", s_max, "let's shear it")
    print("After shearing , here is my flock")
    s = size_sheep.index(s_max)
    size_sheep[s] = 8
    print(size_sheep)
    print("==========================================================")

