#การเช็คข้อความ output -> True, False
name = 'What your name, what color do you like'

result = 'What' in name
#result = 'Whhat' not in name

if result:
    name = name.replace('What', 'ABCD')

print(result)
print(name)
