y1, m1, d1 = [int(e) for e in input().split(' ')]
y2, m2, d2 = [int(e) for e in input().split(' ')]

print(y1, m1, d1)

if y1 < y2:
    print('1')

elif y2 < y1:
    print('2')

elif y1 == y2:
    print('equal')
    
    if m1 < m2:
        print('1')
    else:
        print('2')

elif m1 == m2:
    if d1 < d2:
        print('1')
    else:
        print('2')
