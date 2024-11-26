# Greatest Common Divisor (GCD) Implementation using Euclidean Algorithm

# Prompt user to input two integers
a = int(input())  # First number
b = int(input())  # Second number

# Euclidean Algorithm for finding GCD
# This algorithm is based on the principle that the greatest common divisor 
# of two numbers does not change if the smaller number is subtracted from the larger number

while not b==0:
    # Store the current value of b before modification
    old_b = b
    
    # Calculate the remainder when a is divided by b
    # This is the key step in the Euclidean algorithm
    b = a % b
    
    # Update a with the previous value of b
    a = old_b

# Print the final value of a, which is the GCD
print(a)

# Detailed Algorithm Breakdown:

# Example Walkthrough:
# Let's say a = 48, b = 18
# Iteration 1:
#   old_b = 18
#   b = 48 % 18 = 12
#   a = 18
# Iteration 2:
#   old_b = 12
#   b = 18 % 12 = 6
#   a = 12
# Iteration 3:
#   old_b = 6
#   b = 12 % 6 = 0
#   a = 6
# Loop terminates, GCD is 6

# Mathematical Principle:
# GCD(a,b) = GCD(b, a mod b)
# The algorithm repeatedly replaces (a,b) with (b, a mod b)
# until the remainder becomes 0

# Key Characteristics:
# 1. Efficient algorithm for finding GCD
# 2. Works with positive integers
# 3. Time complexity: O(log(min(a,b)))
# 4. Uses modulo operation instead of repeated subtraction

# Alternate Implementations:
# 1. Recursive Version:
'''
def gcd_recursive(a, b):
    return a if b == 0 else gcd_recursive(b, a % b)
    '''

# 2. Using math module:
# import math
# result = math.gcd(a, b)

# Error Handling (Recommended Addition):
'''
def robust_gcd():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        # Handle negative numbers
        a, b = abs(a), abs(b)
        
        # Swap if b is larger
        if b > a:
            a, b = b, a
        
        while b != 0:
            a, b = b, a % b
        
        return a
    
    except ValueError:
        print("Please enter valid integers")
        return None
        '''

# Properties of GCD:
# 1. GCD(a,0) = |a|
# 2. GCD(a,b) = GCD(b,a)
# 3. GCD(a,b) = GCD(|a|,|b|)
# 4. If a = bq + r, then GCD(a,b) = GCD(b,r)

# Real-world Applications:
# 1. Simplifying fractions
# 2. Cryptography algorithms
# 3. Computer algebra systems
# 4. Number theory problems

# Performance Considerations:
# - More efficient than naive methods
# - Works well for large numbers
# - Minimal computational complexity

# Common Pitfalls to Avoid:
# 1. Not handling negative numbers
# 2. Not using absolute values
# 3. Overlooking edge cases

# Learning Objectives:
# - Understand recursive mathematical algorithms
# - Learn modulo operation usage
# - Explore number theory concepts

# Suggested Exercises:
# 1. Implement GCD with different methods
# 2. Add input validation
# 3. Create a function version
# 4. Explore extended Euclidean algorithm

# Additional Variations:
'''
def gcd_with_logging(a, b):
    steps = 0
    print(f"Initial values: a = {a}, b = {b}")
    while b != 0:
        steps += 1
        print(f"Step {steps}: a = {a}, b = {b}")
        a, b = b, a % b
    print(f"GCD found in {steps} steps")
    return a
    '''

# Recommended Best Practices:
# - Add input validation
# - Handle edge cases
# - Consider creating a reusable function
# - Add optional logging or debugging


'''
Comprehensive Analysis:

Algorithm Mechanism
Uses Euclidean algorithm for GCD calculation
Repeatedly applies modulo operation
Reduces numbers until remainder is zero
Core Logic
b = a % b: Calculate remainder
a = old_b: Update a with previous b
Continues until b becomes zero
Mathematical Principle
GCD(a,b) = GCD(b, a mod b)
Progressively reduces problem size
Guarantees finding greatest common divisor
Computational Efficiency
O(log(min(a,b))) time complexity
Minimal computational steps
Works with large numbers
Key Variations Demonstrated
Iterative implementation
Recursive approach
Robust error handling version
Logging-enabled version
Learning Highlights:

Modulo operation
Iterative algorithm design
Number theory concepts
Efficient problem-solving technique
Recommended Next Steps:

Implement multiple GCD solutions
Add comprehensive error handling
Explore advanced number theory algorithms
Practice with different input scenarios
'''