#add
def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("The answer is {}".format(a+b))

#subtract
def subtract():
    a = float(input("enter first number "))
    b = float(input("Enter second number: "))
    print("The answer is {}".format(a-b))

#multiply
def multiply():
    a = float(input("enter first number "))
    b = float(input("Enter second number: "))
    print("The answer is {}".format(a*b))

#divide
def divide():
    a = float(input("enter first number "))
    b = float(input("Enter second number: "))
    print("The answer is {}".format(a/b))

operation = input("pick an operation(+,-,*,/): ")

if operation == '+':
    add()

elif operation == '-':
    subtract()

elif operation == '/':
    divide()

elif operation == '*':
    multiply()

else:
    print("ERROR! operation not available")