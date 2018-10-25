""" BMI = mass(kg) / (height(m) x height(m))
Note: you must do the conversion from cm to m before calculation

Then based on the BMI, tell them that they are:
Severely underweight if BMI < 16
Underweight if BMI is between 16 and 18.5
Normal if BMI is between 18.5 and 25
Overweight if BMI is between 25 and 30
Obese if BMI is more than 30
"""
t = int(input("Nhap chieu cao theo cm:"))
w = int(input("Nhap can nang theo kg:"))
h=t/100
bmi = w/(h*h)
print("BMI cua ban la:",bmi)
if bmi<16:
    print("Ban qua gay")
elif 16<bmi<18.5:
    print("Ban hoi gay")
elif 18.5<bmi<25:
    print("Ban hoi bi chuan day")
elif 255<bmi<30:
    print("Ban hoi beo")
else:
    print("Ban qua beo")
