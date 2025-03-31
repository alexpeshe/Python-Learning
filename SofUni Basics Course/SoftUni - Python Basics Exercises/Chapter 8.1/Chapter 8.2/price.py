# Ticket Combination Prize Calculator

"""
This program finds a specific ticket combination based on a given position and calculates its prize. Let me explain the code with detailed comments:
"""

# Get input from the user - the position of the ticket combination to find
n = int(input())

# Initialize a counter to keep track of how many combinations we've processed
counter = 0

# Loop through all possible values for the first character of the ticket (name_s)
# Starting from 'B' (ASCII 66) up to 'L' (ASCII 76), taking only every other letter (step 2)
# This will give us: B, D, F, H, J, L
for name_s in range(ord('B'), ord('L') + 1, 2):
    
    # Loop through all possible values for the second character of the ticket (sector)
    # Starting from 'f' (ASCII 102) down to 'a' (ASCII 97)
    # This will give us: f, e, d, c, b, a
    for sector in range(ord('f'), ord('a') - 1, -1):
        
        # Loop through all possible values for the third character of the ticket (entrance)
        # From 'A' (ASCII 65) to 'C' (ASCII 67)
        # This will give us: A, B, C
        for entrance in range(ord('A'), ord('C') + 1):
            
            # Loop through all possible values for the fourth character of the ticket (row_num)
            # From 1 to 10
            for row_num in range(1, 11):
                
                # Loop through all possible values for the fifth character of the ticket (seat)
                # From 10 down to 1
                for seat in range(10, 0, -1):
                    
                    # Increment the counter for each combination
                    counter += 1
                    
                    # Check if we've reached the desired position
                    if counter == n:
                        # Calculate the prize as the sum of ASCII values and numbers
                        sum = name_s + sector + entrance + row_num + seat
                        
                        # Print the ticket combination, converting ASCII values back to characters
                        print(f"ticket combination: {chr(name_s)}{chr(sector)}{chr(entrance)}{(row_num)}{(seat)}")
                        
                        # Print the prize amount
                        print(f"Prize: {sum} lv.")

# Concepts Learned

"""

Nested Loops: The program uses five nested loops to generate all possible ticket combinations according to specific patterns.

ASCII Character Handling:

ord() function is used to convert characters to their ASCII values for loop control

chr() function is used to convert ASCII values back to characters for output

Range Function with Different Parameters:

Positive step: range(ord('B'), ord('L') + 1, 2) - increments by 2

Negative step: range(ord('f'), ord('a') - 1, -1) - decrements by 1

Standard range: range(1, 11) - increments by 1 from start to end-1

Counter Pattern: The program uses a counter to keep track of the current position in the sequence of all possible combinations.

Conditional Exit: The program stops processing once it finds the combination at the specified position.

String Formatting: F-strings are used to format the output, combining both character and numeric values.

Arithmetic with ASCII Values: The prize calculation adds ASCII values of characters with numeric values.

Systematic Enumeration: The code systematically enumerates all possible combinations according to specific rules:

First character: Even letters from B to L

Second character: Letters from f down to a

Third character: Letters from A to C

Fourth character: Numbers from 1 to 10

Fifth character: Numbers from 10 down to 1

This program demonstrates how to generate and process a large number of combinations in a systematic way, and how to find a specific item in that sequence based on its position"""