item=["pho","chao","com rang"]
# new_mon = input("Nhap mon an ua thich: ")
# item.append(new_mon)

print(item,sep="\n")

i = int(input("Vi tri ban muon update: ?"))

new_value = input("Thay the thanh: ")
item[i] = new_value
print(*item,sep='\n')
