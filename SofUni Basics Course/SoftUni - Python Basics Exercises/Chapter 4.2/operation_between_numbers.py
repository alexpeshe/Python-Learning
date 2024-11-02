# Get user input for numbers and operator
n1 = int(input())  # First number
n2 = int(input())  # Second number
operator = input()  # Mathematical operator (+, -, *, /, %)

# Initialize variables
result = 0
output = ""

# Check for division by zero error
if n2 == 0 and (operator == "/" or operator == "%"):
    output = f"Cannot divide {n1} by zero"

# Handle division operation
elif operator == "/":
    result = n1 / n2
    output = f"{n1} {operator} {n2} = {result:.2f}"  # Format result to 2 decimal places

# Handle modulus operation
elif operator == "%":
    result = n1 % n2
    output = f"{n1} {operator} {n2} = {result:.2f}"  # Format result to 2 decimal places

# Handle basic arithmetic operations (+, -, *)
else: 
    if operator == "+":
        result = n1 + n2  # Addition
    elif operator == "-":
        result = n1 - n2  # Subtraction
    elif operator == "*":
        result = n1 * n2  # Multiplication
    
    # Format output string with result and check if result is even or odd
    output = f"{n1} {operator} {n2} = {result}" + f" - {'even' if result % 2 == 0 else 'odd'}"

# Display the final result
print(output)