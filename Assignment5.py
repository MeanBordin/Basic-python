#โปรแกรมการทอนเงิน 
number = int(input('Enter :'))

if number >= 1000:
    print('1000 บาท = ',number//1000,' ใบ')
    number %= 1000

if number >= 500:
    print('500 บาท = ',number//500,' ใบ')
    number %= 500

if number >= 100:
    print('100 บาท = ',number//100,' ใบ')
    number %= 100

