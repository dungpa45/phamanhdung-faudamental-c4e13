p_list = [
    {
        'name': 'Huy',
        'hours': 30,
        'luong': 50,
    },
    {
        'name': 'Quan',
        'hours': 20,
        'luong': 40,
    },
    {
        'name': 'Duc',
        'hours': 15,
        'luong': 65,
    }
]

for p in p_list:
    print(p['name'],p['luong'])

# tinh luong tung ng
print("Luong cua tung ng la:")
for p in p_list:
    l=p['luong']*p['hours']
    print(p['name'], l)

#tinh tong luong
print("Tong luong la:")
t=0
for p in p_list:
    l = p['luong']*p['hours']
    t=t+l
print(t)
