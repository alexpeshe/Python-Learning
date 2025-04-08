# Read input
n = input() # start letter
l = input() # end letter 
m = input() # skip letter

# Convert to ASCII
start_ascii = ord(n)
end_ascii = ord(l)
skip_ascii = ord(m)

# Initialize counter
count = 0

# Generate combinations with 3 nested loops
for letter1 in range(start_ascii, end_ascii + 1):
    for letter2 in range(start_ascii, end_ascii + 1):
        for letter3 in range(start_ascii, end_ascii + 1):

# For each letter position...
    # Check if current combination contains skip_letter
    # Check if none of the letters match skip_ascii
            if letter1 != skip_ascii and letter2 != skip_ascii and letter3 != skip_ascii:
                # This is a valid combination
                print(chr(letter1) + chr(letter2) + chr(letter3), end=' ')
                count += 1  # Increment counter for each valid combination
    # If not, print and increment counter

# Print the final count
print(count)


"""
Certainly! Here's a summary of the key concepts learned from this "Letters Combinations" problem:

ASCII Value Manipulation:

Converting characters to ASCII values using ord()

Converting ASCII values back to characters using chr()

Using ASCII values for character range iterations

Nested Loops:

Implementing triple-nested loops to generate all possible combinations

Understanding how to set correct start and end values for ranges

Character Range Iteration:

Iterating through a range of characters using their ASCII values

Handling inclusive ranges (including both start and end characters)

Filtering and Conditional Logic:

Implementing conditions to exclude specific combinations (those containing the skip letter)

Using multiple conditions in a single if statement

String Concatenation:

Building strings by concatenating individual characters

Counting and Tracking:

Using a counter variable to keep track of valid combinations

Incrementing the counter conditionally

Output Formatting:

Printing multiple items on the same line using end=' ' in print statements

Combining different types of output (combinations and count) in the required format

Input Processing:

Reading and processing multiple lines of input

Converting input characters into usable data (ASCII values)

Problem-Solving Approach:

Breaking down a complex problem into smaller, manageable steps

Translating problem requirements into code logic

Efficiency Considerations:

Understanding the importance of placing conditions correctly to avoid unnecessary iterations or checks

These concepts collectively demonstrate skills in string manipulation, looping constructs, conditional logic, and basic algorithm design in Python."""