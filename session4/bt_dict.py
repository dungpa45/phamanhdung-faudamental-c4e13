day = {
    'monday':'Thu 2',
    'tuesday':'Thu 3',
    'wednesday':'Thu 4',
    'thursday':'Thu 5',
    'friday':'Thu 6',
    'saturday':'Thu 7',
    'sunday':'Chu nhat'
}
print('monday',
      'tuesday',
      'wednesday',
      'thursday','friday','saturday','sunday',sep=", ")

while True:
    
    n = input("Nhap cac tu tren de xem nghia: ")
    if n in day:
        print("Nghia la:",day[n])
        
    else:
        print("not found")
    
        c= input("do u want contribute this word?(Y/N)?")
        if c=='y'or c=='Y':
            new=input("Enter your translation:")
            day[n]= new
            print("update")
        elif c=='n'or c=="N":
            print("Thanks")
            break
        else:
            print("Sai cu phap")
            