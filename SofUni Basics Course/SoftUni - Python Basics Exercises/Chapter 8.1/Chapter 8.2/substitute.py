# Football Team Substitution Program

"""
This program simulates player substitutions in a football match, where players are identified by two-digit numbers. Let me explain the code with detailed comments:
"""

# Get input from the user - these represent the constraints for player numbers
k = int(input())  # Starting value for the first digit of the first player
l = int(input())  # Starting value for the second digit of the first player
m = int(input())  # Starting value for the first digit of the second player
n = int(input())  # Starting value for the second digit of the second player

# Nested loops to generate all possible combinations of player numbers within constraints
for num_1 in range(k, 8+1):  # First digit of first player: from k up to 8
    for num_2 in range(9, l-1, -1):  # Second digit of first player: from 9 down to l
        for num_3 in range(m, 8+1):  # First digit of second player: from m up to 8
            for num_4 in range(9, n-1, -1):  # Second digit of second player: from 9 down to n
                
                # Check if the player numbers follow the required pattern:
                # - First digits (num_1, num_3) must be even
                # - Second digits (num_2, num_4) must be odd
                if (num_1 % 2 == 0 and not num_2 % 2 == 0) and (num_3 % 2 == 0 and not num_4 % 2 == 0):
                    
                    # Check if we're not trying to substitute a player with themselves
                    # (both digits must be different)
                    if not num_1 == num_3 and not num_2 == num_4:
                        # Valid substitution - print the player numbers
                        print(f"{num_1}{num_2} - {num_3}{num_4}")
                    else:
                        # Invalid substitution - same player
                        print("Cannot change the same player")


# Concepts Learned

'''
Nested Loops: The program uses four nested loops to generate all possible combinations of player numbers within the given constraints.

Range Function with Step Parameter: The second and fourth loops use a negative step (-1) to iterate in descending order from 9 down to the specified limit.

Modulo Operator for Parity Check: The modulo operator (%) is used to check if numbers are even (num % 2 == 0) or odd (not num % 2 == 0).

Logical Operators: The program uses and and not operators to combine multiple conditions.

Conditional Statements: if-else statements are used to apply different logic based on conditions.

String Formatting: F-strings are used to format the output in a readable way, combining variables with text.

Problem Modeling: The code models a specific problem domain (football player substitutions) with specific rules:

Player numbers are two digits

First digit must be even (≤ 8)

Second digit must be odd (≤ 9)

Cannot substitute a player with themselves

Boundary Conditions: The program handles constraints on the range of valid values for each digit of the player numbers.

This program demonstrates how to use nested loops to generate combinations and apply filtering logic to find valid solutions to a specific problem
'''