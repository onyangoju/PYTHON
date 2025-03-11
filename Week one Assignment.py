# Pauline's Math Assistant

print("Welcome to the Pauline's Math Assistant!")  # A friendly greeting

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif operation == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    elif operation == "*":
        return f"{num1} * {num2} = {num1 * num2}"
    elif operation == "/":
        if num2 != 0:
            return f"{num1} / {num2} = {num1 / num2}"
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation. Please choose +, -, *, or /."

try:
    # Ask the user for inputs with validation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()

    # Perform the calculation and print the result
    result = calculate(num1, num2, operation)
    print(result)

except ValueError:
    print("Error: Please enter valid numbers.")

print("Your Maths 911. Use Again!")  # A nice closing
