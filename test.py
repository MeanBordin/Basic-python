#some function for testing 
def print_pass(test_name):
    print(f'{test_name}:\t Pass ✔')

def print_fail(test_name):
    print(f'{test_name}:\t Fail ❌')

def test_mult(func):
    if func(5,6) == 5*6:
        print_pass(func.__name__)
    else:
        print_fail(func.__name__)

def mult_recursive(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + mult_recursive(num1, num2-1)
    
test_mult(mult_recursive)

def mult_loop(num1, num2):
    sum = 0
    for i in range(num2):
        sum += num1
    return sum

test_mult(mult_loop)