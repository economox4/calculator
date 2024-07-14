import math

# Functions

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply (x, y):
    return x*y

def divide (x, y):
    if y == 0:
        print("Error")
    return x/y

def exponent (x, y):
    return x**y

def square_root (x):
    return math.sqrt(x)

def percentage (x, y):
    return x*y /100.0

def pi (x):
    return  math.pi (x)

# User_input

operation = input("Opearations (+, -, *, /, ^, √, %, ac, π, exit)")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# Operations

if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
elif operation == "^":
    result = exponent(num1, num2)
elif operation == "√":
    result = square_root(num1, num2)
elif operation == "%":
    result = percentage(num1, num2)
elif operation == "π":
    result = pi(num1, num2)
else:
    result = ("Invanlid Input")

print(f"Result: {result}")


# End

while True:
    user_input = input("Expression: ")
    if user_input.lower() == "ac":
        break
    elif user_input.lower() == "exit":
        exit