# BMI = wight (kg) / hight (m)

#input
wight = int(input("Enter you wight(KG) : ")) #convert to integer
high = int(input("Enter you high(M) : "))

#prosess
high /= 100 
bmi = wight / (high**2)

if bmi < 18.5:
    print('+-------------------+')
    print('| '+str(bmi))
    print('| '+'น้ำหนัก ต่ำกว่าเกณ')
elif bmi >= 18.5 and bmi <= 24.9:
    print('+-------------------+')
    print('| '+str(bmi))
    print('| '+'น่ำหนักปกติ')
elif bmi >= 25 and bmi <= 29.9:
    print('+-------------------+')
    print('| '+str(bmi))
    print('| '+'น้ำ หนักอ้วน')
elif bmi >= 30:
    print('+-------------------+')
    print('| '+str(bmi))
    print('| '+'น้ำหนักมากกว่าเกณ')
else:
    print('เกิดข้อผิดพลาด')

#output
print('+-------------------+')
