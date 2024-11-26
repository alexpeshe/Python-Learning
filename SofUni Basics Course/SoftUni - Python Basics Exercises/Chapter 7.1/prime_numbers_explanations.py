# Import the math module to use mathematical functions
import math

# Prompt user to input a number and convert it to an integer
n = int(input())

# Initialize a flag to assume the number is prime
is_prime = True

# Check if the number is less than 2 (which are not prime)
if n < 2:
    print("Not prime")
else:
    # Calculate the square root of n to optimize prime checking
    # We only need to check divisors up to the square root of n
    end_i = int(math.sqrt(n))

    # Iterate through potential divisors from 2 to square root of n
    for num in range(2, end_i+1):
        # Check if n is divisible by the current number
        # Using integer division to check for exact division
        if n/num == n//num:
            # If divisible, set is_prime to False and break the loop
            is_prime = False

    # Print the result based on the prime flag
    if is_prime:
        print('Prime')
    else:
        print('Not prime')

# print(is_prime)

#SoftUni's alternative solution

'''
Key Points and Analysis:

Prime Number Check Algorithm:

The code implements a basic prime number checking algorithm
It checks for divisibility of the number up to its square root
Time complexity is O(√n)
Optimization Techniques:

Uses square root to reduce unnecessary iterations
Stops checking as soon as a divisor is found
Potential Improvements:

Handle edge cases more explicitly
Add input validation
Consider more efficient prime checking algorithms for large numbers
'''

'''
Comprehensive Analysis:

Strengths:

Simple and straightforward implementation
Efficient for small to medium-sized numbers
Uses mathematical optimization (square root)
Weaknesses:

Not the most efficient for very large numbers
Lacks comprehensive input validation
Doesn't handle negative numbers explicitly
Recommendations:

Add input validation
Handle negative numbers
Consider more advanced prime checking algorithms for large numbers
Add error handling for invalid inputs

'''
# Improved Version:

'''
import math

def is_prime(n):
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if n < 2:
        return False
    
    # Optimize for 2 and even numbers
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisibility up to square root
    end_i = int(math.sqrt(n))
    for num in range(3, end_i + 1, 2):
        if n % num == 0:
            return False
    
    return True

# Example usage with error handling
try:
    number = int(input("Enter a number to check for primality: "))
    print("Prime" if is_prime(number) else "Not Prime")
except ValueError as e:
    print(f"Error: {e}")
    '''
'''
This improved version addresses the previous limitations by:

Adding input validation
Handling edge cases more robustly
Improving performance for even numbers
Using a more pythonic approach with a dedicated function
Adding error handling

'''
# Alternative Version:

'''
# Import math module for mathematical operations
import math

# Set initial assumption that the number is prime
prime = True

# Iterate through potential divisors from 2 to square root of n
for i in range(2, int(math.sqrt(n))):
    # Check if the number is divisible by the current iterator
    if n % i == 0:
        # If divisible, set prime flag to False
        prime = False
        # Immediately exit the loop when a divisor is found
        break

# Check the final state of the prime flag
if prime:
    # If prime remains True, print Prime
    print('Prime')
else:
    # If prime was set to False, print Not Prime
    print('Not prime')
    '''

'''
Key Points and Analysis:

Prime Number Checking Algorithm:

Implements a basic primality test
Checks divisibility up to the square root of the number
Uses a flag-based approach to determine primality
Algorithmic Characteristics:

Time Complexity: O(√n)
Space Complexity: O(1)
Early termination when a divisor is found
Comprehensive Analysis:

Strengths:

Simple and straightforward implementation
Efficient for small to medium-sized numbers
Uses square root optimization
Breaks early when a divisor is found
Weaknesses:

Doesn't handle edge cases explicitly
No input validation
Assumes n is already defined
'''
# Improved Version:

'''
import math

def is_prime(n):
    # Handle edge cases
    if n < 2:
        return False
    
    # Special case for 2 (only even prime)
    if n == 2:
        return True
    
    # Quickly eliminate even numbers > 2
    if n % 2 == 0:
        return False
    
    # Check divisibility up to square root
    # Use int(math.sqrt(n)) + 1 to ensure full coverage
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # Check for divisibility
        if n % i == 0:
            return False
    
    # If no divisors found, it's prime
    return True

# Robust implementation with error handling
def check_prime():
    try:
        # Get input with type conversion and validation
        n = int(input("Enter a number to check for primality: "))
        
        # Use the is_prime function to determine primality
        if is_prime(n):
            print(f"{n} is Prime")
        else:
            print(f"{n} is Not Prime")
    
    except ValueError:
        print("Please enter a valid integer")

# Run the prime checking function
check_prime()
'''

'''
Recommendations:

Separate Concerns:

Create a dedicated function for prime checking
Add input validation
Handle edge cases explicitly
Performance Improvements:

Check even numbers first
Only check odd divisors
Use early termination
Error Handling:

Add input type checking
Provide meaningful error messages
Handle potential exceptions
Optimization Techniques:

Use range(3, int(math.sqrt(n)) + 1, 2) to check only odd numbers
Add special case handling for 2 and even numbers
Additional Considerations:

For very large numbers, consider more advanced primality tests
Implement probabilistic primality tests for extremely large numbers
Consider using libraries like sympy for advanced prime checking
Example Advanced Usage:
'''

# Example Advanced Usage:

'''
# For extremely large numbers
import sympy

def advanced_prime_check(n):
    # Use probabilistic primality test
    return sympy.isprime(n)

# Benchmark and compare different prime checking methods
def compare_prime_methods(n):
    import timeit
    
    # Compare custom implementation vs sympy
    custom_time = timeit.timeit(lambda: is_prime(n), number=1000)
    sympy_time = timeit.timeit(lambda: sympy.isprime(n), number=1000)
    
    print(f"Custom Method Time: {custom_time}")
    print(f"SymPy Method Time: {sympy_time}")
    '''

'''
Learning Points:

Primality testing is a fundamental algorithmic problem
Optimization is crucial for efficiency
Different approaches suit different scales of numbers
Always consider edge cases and input validation
The improved version addresses the original code's limitations by:

Adding comprehensive error handling
Improving performance
Providing a more robust and flexible implementation
Separating the prime checking logic into a reusable function
'''