'''
if expresstion :
    statement
'''

#input
age = (input("Enter your age :"))
age = int(age)
#process
if age >= 15:
    print('นาย/นางสาว\n') 
elif  age > 0 and age <= 15:
    print('เด็กชาย/เด็กหญิง')

print("จบโปรแกรม")