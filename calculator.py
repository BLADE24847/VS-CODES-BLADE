def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

user_input = input("if you want to add, substract, multiply or divide any two numbers then type it like 'number followed by operator followed by number'-----  ")

num1, operator , num2 = user_input.split()

num1 = float(num1)
num2 = float(num2)

if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(substract(num1,num2))
elif operator == "*":
    print(multiply(num1,num2))
elif operator == "/":
    print(divide(num1,num2))
else:
    print("Sorry I cannot do that")
