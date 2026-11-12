a = int(input("enter a number: "))
b = int(input("enter another number: "))
try:
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")