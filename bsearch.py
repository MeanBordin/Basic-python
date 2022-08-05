def bSearch(index_d, left, right, x):

	if right >= left:

		mid = left + (right - left) // 2

		if index_d[mid] == x:
			return mid

		elif index_d[mid] > x:
			return bSearch(index_d, left, mid-1, x)


		else:
			return bSearch(index_d, mid + 1, right, x)

	else:
		return -1


# input form user
d = input('Enter elements of a list separated by space : ')
index_d = d.split()
x = 10

print('List: ',index_d)

for i in range(len(index_d)):
    index_d[i] = int(index_d[i])
 

# Function call
result = bSearch(index_d, 0, len(index_d)-1, x)

#display
if result != -1:
	print("Element is present at index % d" % result)
else:
	print("Element is not present in array")
