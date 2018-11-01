print("Answer the following algebra question: ")
print()
question ={
    "If x = 8, then what is the value of 4(x+3) ?":[35,36,40,44],
    "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?": ['About 55','About 65','About 75','About 85'],
    "H2 + O2 -> ?":['HOHO','(OH)2','H2O','HO']

}
answer = {
    "If x = 8, then what is the value of 4(x+3) ?":4,
    "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?": 2,
    "H2 + O2 -> ?": 3
}

correct = 0

for ch in question:
    print(ch)
    for i in question[ch]:
        print(i)
    while True:
        print("You are only selected 1,2,3,4")
        choice = int(input("Your choice: "))

        if choice == answer[ch]:
            print("*******Bingo*******")
            correct+=1
            break
        else:
            print(":( Try again :(")
            break

print("You correctly answer",correct,"out of", len(question) ,"question")
