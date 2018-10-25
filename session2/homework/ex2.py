#Asks users enter a number and then calculates factorial of n: (1 * 2 * 3 *... *n)
n = int(input("Nhap 1 so bat ky "))
tich= 1
for i in range(1,n+1):
    tich *= i
print("Tich tu 1 den",n,"la",tich)