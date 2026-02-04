num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operation = input("Enter Operation (+, -, *, /): ") 

# addition
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

# subtraction
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

# multiplication
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

# division
elif operation == '/':
    if num2 != 0:                               # it will check if user enter 0 for second number
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")  # if user enter 0 for second number it will print error message

# it will print invalid operation if user enter other than +, -, *, /
else:
    print("Invalid operation. Please enter +, -, *, or /.")    