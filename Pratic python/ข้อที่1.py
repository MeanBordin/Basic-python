unit = int(input('Enter unit : '))
price = float(input('Enter price : '))
member = input('Are your is member y(yes) / n(no) : ')

total = unit * price
discount, amount = 0, 0

if member == 'y':
    
    if total <= 500:
        discount = ( total * 10 )/ 100
    
    elif total > 500 and total < 1000:
        discount = total * 0.15

    elif total > 1000:
        discount = total * 0.2

elif member == 'n':
    
    if total <= 500:
        discount = total * 0.05

    elif total > 500 and total < 1000:
        discount = total * 0.1
    
    elif total > 1000:
        discount = total * 0.15

amount = total - discount

print('Total :' ,total)
print('Discount :' ,discount)
print('Amount :' ,amount)
