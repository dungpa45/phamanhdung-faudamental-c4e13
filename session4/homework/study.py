dem_chu = {}
chuoi = input("Nhap vao 1 cau bat ky: ").lower()

for chu in chuoi:
    dem_chu[chu]= dem_chu.get(chu, 0)+1

xep_chu = list(dem_chu.items())
xep_chu.sort()

for k,v in xep_chu:
    print(k,v)
    
