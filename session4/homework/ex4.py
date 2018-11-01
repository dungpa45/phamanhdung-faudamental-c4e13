print("Answer the following algebra question: ")
print("If x = 8, then what is the value of 4(x+3) ?")
answer = {
    '1':35,
    '2':36,
    '3':40,
    '4':44,
}

for k, v in answer.items():
    print(k,v,sep=". ")

choice=input("Your choice: ")
if choice == '4':
    print("Bingo")
else:
    print(":(")
