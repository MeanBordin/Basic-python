#law Variable name
'''
1.ห้ามขึ้นต้นด้วยตัวเลข และสัญลักษณ์ ยกเว้น _ 
2.Keybord = if, else, while, ...
3.Case sensitive = ตั้งชื่อตัวแปรสื่อความหมาย
'''

'''
Type Coversion 
'''

number = 20
name = "Bordinsak"
bo_ol = True
str_num = "100" 
print('Bordinsak' + 'Prasopboon')
print('Bordinsak' + str(number))
print('______________________')
print(type(number))
print(type(name))
print(type(bo_ol))
print('______________________')
result = str(number)+str_num
print(result)
print('______________________')
'''
change string to int
int(Variable)
float(Variable)
str(Variable)
'''
print("Chang string to intiger")
#str_num = int(str_num) แปลงแบบ ถาวร
chang_str = int(str_num) 
print("Tpye = ",type(str_num),"Change ->",type(chang_str),str(chang_str))
