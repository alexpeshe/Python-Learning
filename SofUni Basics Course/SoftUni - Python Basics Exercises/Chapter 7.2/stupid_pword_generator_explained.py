# Get input for total number of digits/values
n = int(input())

# Get input for length of letter range
l = int(input())

# Starting ASCII value for lowercase letters (a = 97)
start_letter = 97 

# Calculate end of letter range 
end_letter = start_letter + l

# Nested loops to generate a specific pattern of combinations
for num1 in range(1, n):                   # First numeric digit
    for num2 in range(1, n):                # Second numeric digit
        for num3 in range(start_letter, end_letter):  # First letter
            for num4 in range(start_letter, end_letter):  # Second letter
                for num5 in range(1, n+1):   # Final numeric digit
                    # Condition: last digit must be larger than first two digits
                    if num5 > num1 and num5 > num2:
                        # Print combination with space separator
                        print(str(num1) + str(num2) + chr(num3) + chr(num4) + str(num5), end=' ')


'''
Key Points and Analysis:
------------------------
Purpose of the Code:
------------------------

Generates combinations of numbers and letters with specific constraints
Creates a pattern of 5-character strings

Input Parameters:
------------------------

n: Defines the range for numeric digits (1 to n-1 or 1 to n)
l: Determines the range of letters to be used

Combination Structure:
------------------------

First two characters: Numeric digits (1 to n-1)
Third character: First letter (from ASCII range)
Fourth character: Second letter (from ASCII range)
Fifth character: Numeric digit (1 to n, with condition)

Unique Constraints:
------------------------
- Last digit must be larger than the first two digits
Last digit must be larger than first two digits
Uses ASCII conversion for letters
Nested loops for comprehensive combination generation
'''

'''
Recommendations:
------------------------
Performance Optimization:
------------------------
The nested loops can be computationally expensive for large n and l
Consider using itertools or generator functions for more efficient combination generation

Error Handling:
------------------------
Add input validation to ensure n and l are positive integers
Handle potential overflow or large input scenarios

Flexibility Improvements:
------------------------
Make letter range customizable
Add option to control output format
Implement filtering mechanisms
'''

# Example Enhanced Version:

'''
def generate_combinations(n, l, start_letter=97):
    """
    Generate combinations with configurable parameters
    
    Args:
        n (int): Range for numeric digits
        l (int): Letter range length
        start_letter (int): Starting ASCII value for letters
    """
    end_letter = start_letter + l
    
    combinations = [
        f"{num1}{num2}{chr(letter1)}{chr(letter2)}{num5}"
        for num1 in range(1, n)
        for num2 in range(1, n)
        for letter1 in range(start_letter, end_letter)
        for letter2 in range(start_letter, end_letter)
        for num5 in range(1, n+1)
        if num5 > num1 and num5 > num2
    ]
    
    return combinations

# Usage
result = generate_combinations(5, 3)
print(*result)
'''

'''
Potential Use Cases:
------------------------

Pattern generation
Combinatorial problem solving
Algorithmic challenges
Educational demonstrations of nested loop logic
Time Complexity: O(n^4 * l^2) Space Complexity: Depends on output storage method
--------------------------------------------------------------------------------
Caution: Be mindful of computational resources for large input values.'''