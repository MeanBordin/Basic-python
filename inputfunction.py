first_name, last_name = [str(i) for i in input("Enter your first name and last name : ").split(',')]
number_1, number_2 = [int(i) for i in input("Enter your number : ").split(',')]

result_1 = first_name +' '+ last_name
result_2 = number_1+number_1

print("Full name = "+result_1)
print("Result = "+str(result_2))
