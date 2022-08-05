#ตัวดำเนินการทางคณิตศาสตร์

x = 10 #ตัวถูกดำเนิดการ
y = 5

#ตัวดำเนิดการ
result_1 = x+y
result_2 = x-y
result_3 = x*y
result_4 = x/y
result_5 = x//y #หารปัดเศษ
result_6 = x%y #หารเอาเศษ
result_7 = x**y #ยกกำลัง

print("Result = "+str(result_1))
print("Result = "+str(result_2))
print("Result = "+str(result_3))
print("Result = "+str(result_4))
print("Result = "+str(result_5))
print("Result = "+str(result_6))
print("Result = "+str(result_7))

'''
print("________________________________")
ตัวดำเนิดการเปรียบเทียบ 
คำตอบ = True/False
'''

print("X>Y -> ",x>y)
print("X<Y -> ",x<y)
print("X==Y -> ",x==y)
print("X!=Y -> ",x!=y)
print("X>=Y -> ",x>=y)
print("X<=Y -> ",x<=y)
print("________________________________")

#ตัวดำเนินการทางตรรกศาสตร์
'''
AND 
OR
NOT
'''
num1 = (5>10)
num2 = (10==5)
# and -> T and T = T 
print("-AND-")
a = (5>10) and (10==5)
print(a)
print("__________")
# or -> F or F = F
print("-OR-")
b = (5>10) or (10!=5)
print(b)
print("__________")
print("-NOT-")
c = (5>10) and (10==5)
print(not c)
d = (5>10) or (10==5)
print(not d)