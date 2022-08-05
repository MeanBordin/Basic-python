age = int(input('Enter your age : '))

if age <= 15:
    if age == 15:
        print('ม.3')
    elif age == 14:
        print("ม.4")
    elif age == 13:
        print('ม.1')
    else:
        print('ประถมศึกษา')
else:
    print('ม.ปลาย')

print('End program.')
