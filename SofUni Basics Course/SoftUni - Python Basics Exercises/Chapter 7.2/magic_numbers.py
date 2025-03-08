# Get user input for target number
n = int(input())    # Convert string input to integer
result = ''         # Initialize empty string to store results

# Nested loops to generate 6-digit combinations
for a in range(1, 10):          # First digit: 1-9
    for b in range(1, 10):      # Second digit: 1-9
        for c in range(1, 10):  # Third digit: 1-9
            for d in range(1, 10):  # Fourth digit: 1-9
                for e in range(1, 10):  # Fifth digit: 1-9
                    for f in range(1, 10):  # Sixth digit: 1-9
                        # Check if multiplication of digits equals target number
                        # Note: d**e means d raised to power e
                        if a*b*c*d**e*f == n:
                            # If condition met, concatenate digits to result string
                            result += ('' + str(a) + str(b) + str(c) + str(d) + str(e) +str(f) + '')

# Print all found combinations
print(result)

'''
Key Points:
Purpose: The code finds all 6-digit numbers where a specific mathematical operation on their digits equals a target number.

Operation: Multiplies first 3 digits, then fourth digit raised to power of fifth digit, then multiplied by sixth digit

Range: Checks all combinations of digits 1-9 (not including 0)

Output: Concatenates all valid combinations into a single string

Comprehensive Analysis:
Complexity
Time Complexity: O(9⁶) - six nested loops

Space Complexity: O(k) where k is number of valid combinations

Total iterations: 9⁶ = 531,441 combinations checked

Performance Considerations
Very computationally intensive due to nested loops

Memory usage is efficient (only stores valid results)

May be slow for large target numbers

Limitations
Doesn't include 0 in digit possibilities

May overflow for large exponents

All results concatenated without separators

No error handling for invalid inputs

'''

'''
Recommendations:
Performance Improvements

# Add early exit conditions
if n <= 0:
    print("Number must be positive")
    exit()

Better Result Formatting:

# Store results in list and join with spaces
results = []
...
results.append(f"{a}{b}{c}{d}{e}{f}")
print(" ".join(results))

Input Validation:

try:
    n = int(input())
    if n <= 0:
        raise ValueError("Number must be positive")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

Memory Optimization:

# Use generator instead of storing all results
def magic_numbers(n):
    for a in range(1, 10):
        # ... nested loops ...
        if a*b*c*d**e*f == n:
            yield f"{a}{b}{c}{d}{e}{f}"

Additional Features:

Add progress indicator for long calculations

Include option to limit search range

Add explanation of found results

Include option to show calculation details

'''

# Complete Enhanced Version:

'''
def find_magic_numbers(target):
    if not isinstance(target, int) or target <= 0:
        raise ValueError("Target must be a positive integer")
    
    results = []
    total_combinations = 0
    
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            total_combinations += 1
                            if a*b*c*d**e*f == target:
                                results.append(f"{a}{b}{c}{d}{e}{f}")
                                
    return results, total_combinations

try:
    n = int(input("Enter target number: "))
    results, combinations = find_magic_numbers(n)
    print(f"\nFound {len(results)} magic numbers")
    print(f"Checked {combinations} combinations")
    print("Results:", " ".join(results) if results else "None found")
except ValueError as e:
    print(f"Error: {e}")
'''
