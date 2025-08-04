# Simple calculator for beginners

while True:
    # Get input and convert to float
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please enter one of +, -, *, or /.")

    # Ask the user if they want to continue
    choice = input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != 'yes':
        print("Goodbye!")
        break
