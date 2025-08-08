# Task 1: Perform Basic Mathematical Operations

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"

# Display results
print("Results of the operations:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
