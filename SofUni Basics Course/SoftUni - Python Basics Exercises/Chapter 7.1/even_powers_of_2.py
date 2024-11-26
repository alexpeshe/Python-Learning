# Prompt the user to input a number and convert it to an integer
n = int(input())

# Loop through numbers from 0 to n (inclusive)
# range(0, n+1) creates a sequence: 0, 1, 2, ..., nf


for num in range(0, n+1):
    # Check if the current number is even (divisible by 2 with no remainder)
    # num%2 == 0 means the number is perfectly divisible by 2
    if num%2 == 0:
        # Calculate 2 raised to the power of the current even number
        # pow(2, num) calculates 2^num for even numbers
        a = pow(2, num)
        
        # Print only the powers of 2 for even numbers
        print(a)

# Example:
# If n = 6, the output will be:
# 1   (2^0)
# 2   (2^1)
# 4   (2^2)
# 16  (2^4)
# 64  (2^6)

# Note:
# - Only even numbers (0, 2, 4, 6, ...) are processed
# - Skips odd numbers in the power calculation

'''
Key Points:

Input Handling
n = int(input()) converts user input to an integer
Allows dynamic range based on user's input
Looping
range(0, n+1) creates a sequence from 0 to n
Iterates through each number systematically
Even Number Filtering
num%2 == 0 checks if a number is even
Modulo operator (%) determines divisibility by 2
Only processes even numbers in the sequence
Exponentiation
pow(2, num) calculates powers of 2
Uses built-in Python power function
Generates sequence: 2^0, 2^2, 2^4, etc.
Selective Printing
print(a) outputs only powers of even numbers
Skips calculations for odd numbers
Creates a specific mathematical sequence
Logical Flow
Input → Loop → Condition → Calculation → Output
Demonstrates structured problem-solving approach
Skill Indicators:

Understanding control structures
Applying mathematical concepts in code
Creating selective computational logic
Recommended Next Steps:

Experiment with different conditions
Try more complex mathematical sequences
Explore list comprehensions and generator expressions

Share
New

'''

'''
SoftUni's alternative solution

for num in range(0, n+1, 2):
    a = pow(2, num)
    print(a)
'''