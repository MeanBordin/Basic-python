# ค.ส เป็น พ.ศ
# พ.ศ เป็น ค.ส

number_1, number_2 = [int(i) for i in input('ใส่ ค.ส และ พ.ศ :').split(' ')]

number_1 += 543 
number_2 -= 543 

print('ค -> พ = '+str(number_1)+'\n'+'พ -> ค = '+str(number_2))

