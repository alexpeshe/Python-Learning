# Factorial Calculation Program

# Prompt user to input a number
n = int(input())  # Number for which factorial will be calculated

# Initialize factorial result
fact = 1  # Will store the factorial calculation

# Infinite loop with manual break condition
while True:
    # Multiply current factorial result by current number
    fact *= n
    
    # Decrement n in each iteration
    n -= 1
    
    # Break condition: stop when n is no longer greater than 1
    if not n>1:
        break

# Print final factorial result
print(fact)

# Factorial Calculation Logic:
# Factorial of a number n (n!) is the product of all positive integers less than or equal to n
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120

# Comprehensive Analysis:

# 1. Algorithm Mechanism
# - Uses multiplicative approach
# - Iteratively reduces n while multiplying
# - Continues until n becomes 1 or less

# 2. Loop Characteristics
# - Infinite loop with manual break
# - Uses while True for continuous iteration
# - Manual control of iteration process

# 3. Computational Steps
# For n = 5:
# Iteration 1: fact = 1 * 5 = 5,  n = 4
# Iteration 2: fact = 5 * 4 = 20, n = 3
# Iteration 3: fact = 20 * 3 = 60, n = 2
# Iteration 4: fact = 60 * 2 = 120, n = 1
# Loop breaks when n <= 1

# Key Points:
# - Simple factorial calculation method
# - Modifies input number directly
# - Uses multiplicative reduction

# Potential Limitations:
# 1. Modifies input number (side effect)
# 2. No input validation
# 3. Potential integer overflow for large numbers
# 4. No handling of negative numbers

# Recommended Improvements:

# 1. Safer Factorial Function
'''def calculate_factorial(n):
    # Input validation
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle special cases
    if n == 0 or n == 1:
        return 1
    
    # Factorial calculation
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    
    return fact
    '''

# 2. Alternative Implementations:
# Recursive Approach
'''
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
    '''

# 3. Using Functional Approach
''' 
from math import factorial as math_factorial
'''

# Recommendations:
# 1. Add input validation
# 2. Handle edge cases (0, 1, negative numbers)
# 3. Consider using built-in or library functions
# 4. Be aware of integer overflow limitations
# 5. Choose appropriate implementation based on use case

# Performance Considerations:
# - Iterative approach is generally more memory-efficient
# - Recursive approach can be cleaner but less efficient
# - Built-in functions are optimized

# Error Handling Best Practices:
'''
def robust_factorial():
    try:
        n = int(input("Enter a non-negative integer: "))
        
        # Comprehensive validation
        if n < 0:
            print("Factorial is not defined for negative numbers")
            return None
        
        # Efficient calculation
        result = 1
        for i in range(2, n + 1):
            result *= i
        
        return result
    
    except ValueError:
        print("Please enter a valid integer")
        return None

    '''

# Learning Objectives:
# 1. Understand factorial calculation
# 2. Learn loop control techniques
# 3. Explore different implementation strategies
# 4. Practice input validation
# 5. Recognize computational limitations

# Practical Applications:
# - Combinatorics
# - Probability calculations
# - Permutation and combination problems
# - Mathematical modeling

# Common Pitfalls to Avoid:
# 1. Ignoring input validation
# 2. Not handling edge cases
# 3. Overlooking integer overflow
# 4. Using inefficient algorithms for large numbers

# Suggested Exercises:
# 1. Implement factorial with different methods
# 2. Add comprehensive error handling
# 3. Explore large number handling
# 4. Compare performance of different implementations

# Additional Considerations:
# - For very large numbers, consider using libraries
# - Python's built-in support for large integers helps
# - Be mindful of computational complexity

'''
Comprehensive Analysis Highlights:

Simple, direct factorial calculation
Uses multiplicative reduction
Manual loop control
Potential for side effects and limitations
Recommendations:

Add robust input validation
Handle edge cases
Consider alternative implementations
Be aware of computational limitations
Use built-in or library functions when possible
'''

'''
alternative solution:

# Factorial Calculation - Alternative Solution

# Initialize result variable
result = 1  # Important: Initialize to 1, not 0 to avoid multiplication issues

# Input number for factorial calculation
n = int(input())

# Use range with reverse iteration
# range(n, 0, -1) generates sequence: n, n-1, n-2, ..., 1
for num in range(n, 0, -1):
    # Multiply current result by each number in descending order
    # Sugar syntax for result = result * num
    result *= num  

# Print the final result (Note: this actually prints the last iteration value, not the factorial)
print(num)

# Comprehensive Analysis:

# 1. Algorithm Mechanics
# - Uses for loop instead of while loop
# - Iterates from n down to 1
# - Multiplicative factorial calculation

# 2. Range Function Breakdown
# range(start, stop, step)
# n: starting number
# 0: stop before 0 (exclusive)
# -1: decrement by 1 in each iteration

# Example Walkthrough:
# For n = 5
# Iteration 1: result = 1 * 5 = 5,    num = 5
# Iteration 2: result = 5 * 4 = 20,   num = 4
# Iteration 3: result = 20 * 3 = 60,  num = 3
# Iteration 4: result = 60 * 2 = 120, num = 2
# Iteration 5: result = 120 * 1 = 120, num = 1

# Key Differences from Previous Solution:
# 1. Uses for loop instead of while loop
# 2. More Pythonic approach
# 3. Clearer iteration control

# Potential Improvements:

# 1. Corrected Version with Result Printing
def factorial_calculation(n):
    # Input validation
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle special cases
    if n == 0 or n == 1:
        return 1
    
    # Factorial calculation
    result = 1
    for num in range(n, 0, -1):
        result *= num
    
    return result

# 2. Alternative Implementation
def factorial_with_validation(n):
    try:
        # Comprehensive input handling
        n = int(input("Enter a non-negative integer: "))
        
        # Validate input
        if n < 0:
            print("Factorial is not defined for negative numbers")
            return None
        
        # Efficient calculation
        result = 1
        for num in range(1, n + 1):
            result *= num
        
        return result
    
    except ValueError:
        print("Please enter a valid integer")
        return None

# Key Points:
# 1. Initializing result to 1 is crucial
# 2. Range allows reverse iteration
# 3. Sugar syntax for multiplication
# 4. Simple and readable implementation

# Common Pitfalls:
# 1. Printing num instead of result
# 2. Not handling edge cases
# 3. Potential integer overflow
# 4. Lack of input validation

# Recommendations:
# 1. Always validate input
# 2. Handle special cases (0, 1, negative numbers)
# 3. Consider using built-in or library functions
# 4. Be aware of computational limitations

# Performance Considerations:
# - Efficient for small to medium-sized numbers
# - Clear and readable implementation
# - Slight performance advantage over recursive methods

# Computational Complexity:
# - Time Complexity: O(n)
# - Space Complexity: O(1)

# Learning Objectives:
# 1. Understand range function
# 2. Learn multiplicative iteration
# 3. Explore different factorial calculation methods
# 4. Practice loop control techniques

# Practical Applications:
# - Mathematical calculations
# - Combinatorics
# - Probability problems
# - Algorithm design

# Suggested Exercises:
# 1. Implement error handling
# 2. Create a generic factorial function
# 3. Compare different implementation strategies
# 4. Explore large number handling

# Advanced Variations:
def factorial_with_logging(n):
    print(f"Calculating factorial for {n}")
    result = 1
    for num in range(n, 0, -1):
        print(f"Current iteration: result = {result}, num = {num}")
        result *= num
    return result

# Interesting Observations:
# 1. Python handles large integers gracefully
# 2. No explicit type casting needed
# 3. Flexible and readable implementation

# Potential Extensions:
# 1. Add memoization for repeated calculations
# 2. Implement caching mechanism
# 3. Create more robust error handling

# Debugging Tips:
# 1. Use print statements to track iterations
# 2. Validate input thoroughly
# 3. Handle edge cases explicitly
# 4. Consider performance for large inputs

# Recommended Best Practices:
# - Use meaningful variable names
# - Add comprehensive comments
# - Implement proper error handling
# - Consider performance and readability


'''

'''
Key Differences and Improvements:

More Pythonic approach with for loop
Clear iteration control
Simpler syntax
Easier to read and understand
Recommendations:

Add input validation
Handle edge cases
Print the correct result
Consider performance for large numbers
'''