prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for p in prices:
    print(p)
    print("Prices: ",prices[p])
    print("Stock: ",stock[p])

total = 0

for p in prices:
    gia = prices[p]*stock[p]
    print("Tong",p,"co gia la:",gia)
    total+=gia
print("Tong gia tri cac loai la:",total)
