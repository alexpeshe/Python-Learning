# Digit Sum Calculation - Two Approaches

# Approach 1: String Iteration Method
# User inputs a number as a string
num = input()

# Initialize sum variable
sum = 0

# Iterate through each character in the input
for i in num:
    # Convert each character to integer and add to sum
    sum = sum + int(i)

# Note: This print statement prints the original input, not the sum
print(num)

# Approach 2: Numeric Manipulation Method
'''
# User inputs a number as a string
n = input()

# Initialize sum variable
sum = 0

# Infinite loop with manual break condition
while True:
    # Extract the last digit using modulo operation
    # n % 10 gives the rightmost digit
    sum = sum + (n % 10)
    
    # Integer division to remove the last digit
    # n // 10 removes the rightmost digit
    n = n // 10
    
    # Break condition: stop when no digits remain
    if not n > 0:
        break

# Print the sum using formatted string
print('Sum of digits: %d' % sum)
'''

# Comprehensive Analysis:

# 1. Approach 1: String Iteration Method

# Key Characteristics:
# - Converts input to string
# - Iterates through each character
# - Simple and straightforward
# - Works well with string inputs

# Pros:
# - Readable
# - Easy to understand
# - Works with string and numeric inputs
# - No type conversion needed

# Cons:
# - Less efficient for large numbers
# - Prints original input instead of sum
# - Requires string conversion

# 2. Approach 2: Numeric Manipulation Method

# Key Characteristics:
# - Uses mathematical operations
# - Extracts digits through modulo and division
# - More traditional algorithmic approach
# - Works directly with numeric values

# Pros:
# - More efficient
# - Works directly with numbers
# - Lower memory overhead
# - Suitable for large numbers

# Cons:
# - Slightly more complex logic
# - Requires careful handling of input type

# Detailed Algorithm Breakdown:

# Approach 1 Step-by-Step:
# Input: "12345"
# Iteration 1: sum = 0 + 1 = 1
# Iteration 2: sum = 1 + 2 = 3
# Iteration 3: sum = 3 + 3 = 6
# Iteration 4: sum = 6 + 4 = 10
# Iteration 5: sum = 10 + 5 = 15

# Approach 2 Step-by-Step:
# Input: 12345
# Iteration 1: 
#   sum = 0 + (12345 % 10) = 5
#   n = 12345 // 10 = 1234
# Iteration 2:
#   sum = 5 + (1234 % 10) = 9
#   n = 1234 // 10 = 123
# ... continues until n becomes 0

# Recommended Improvements:
'''
# 1. Robust Input Handling
def calculate_digit_sum(input_value):
    try:
        # Convert input to integer
        num = int(input_value)
        
        # Handle negative numbers
        num = abs(num)
        
        # String-based method
        sum_str = sum(int(digit) for digit in str(num))
        
        # Numeric method
        sum_numeric = 0
        while num > 0:
            sum_numeric += num % 10
            num //= 10
        
        return sum_str, sum_numeric
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None
'''


# 2. More Pythonic Approaches
'''

# Using sum() and map()
def digit_sum_functional(num):
    return sum(map(int, str(num)))

# Recursive Approach
def digit_sum_recursive(num):
    if num < 10:
        return num
    return num % 10 + digit_sum_recursive(num // 10)

# 3. Performance Optimized Version
def efficient_digit_sum(num):
    return sum(int(digit) for digit in str(num))
'''


# Key Recommendations:
# 1. Add input validation
# 2. Handle different input types
# 3. Consider performance for large numbers
# 4. Provide clear error messages
# 5. Choose method based on specific requirements

# Performance Considerations:
# - String method: O(n) time complexity
# - Numeric method: O(log n) time complexity
# - String method uses more memory
# - Numeric method is more memory-efficient

# Common Pitfalls:
# 1. Not handling non-numeric inputs
# 2. Overlooking negative number scenarios
# 3. Inefficient implementations
# 4. Ignoring type conversions

# Learning Objectives:
# 1. Understand digit extraction techniques
# 2. Learn different algorithm approaches
# 3. Practice input handling
# 4. Explore type conversion methods

# Practical Applications:
# - Digital root calculation
# - Checksum algorithms
# - Number theory problems
# - Data validation

# Debugging Tips:
# 1. Add print statements for intermediate values
# 2. Validate input thoroughly
# 3. Test with various input scenarios
# 4. Use type checking

'''
# Extended Example with Comprehensive Handling
def advanced_digit_sum(input_value):
    try:
        # Multiple input type handling
        if isinstance(input_value, str):
            num = int(input_value)
        elif isinstance(input_value, int):
            num = input_value
        else:
            raise ValueError("Unsupported input type")
        
        # Absolute value to handle negative numbers
        num = abs(num)
        
        # Multiple calculation methods
        methods = {
            'string': sum(int(digit) for digit in str(num)),
            'numeric': sum(int(digit) for digit in str(num)),
            'mathematical': sum(int(digit) for digit in str(num))
        }
        
        return methods
    
    except ValueError as e:
        print(f"Error: {e}")
        return None
'''


# Suggested Exercises:
# 1. Implement error handling
# 2. Create a generic digit sum function
# 3. Compare different implementation strategies
# 4. Add logging and debugging capabilities


'''
Comprehensive Comparison:

String Iteration Method
Pros: Simple, readable
Cons: Less efficient, prints input
Numeric Manipulation Method
Pros: Efficient, works with numbers
Cons: Slightly more complex logic
Recommendations:

Validate inputs
Handle different scenarios
Choose method based on requirements
Consider performance needs
'''