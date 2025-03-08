# Get input number
number = int(input())

# Convert to string to get digits
num_str = str(number)
first_digit = int(num_str[0])    # Get first digit
second_digit = int(num_str[1])   # Get second digit
third_digit = int(num_str[2])    # Get third digit

# Calculate rows (N) and columns (M)
N = first_digit + second_digit
M = first_digit + third_digit

# Initialize current number
current = number

# Create grid of N rows and M columns
for row in range(N):
    # Process M numbers for current row
    for col in range(M):
        # Apply the rules
        if current % 5 == 0:
            # If divisible by 5, subtract first digit
            current -= first_digit
        elif current % 3 == 0:
            # If divisible by 3, subtract second digit
            current -= second_digit
        else:
            # Otherwise, add third digit
            current += third_digit
            
        # Print current number with space
        print(current, end=' ')
    
    # New line after each row
    print()

'''
Key Points:
Digit Extraction: Convert number to string to get individual digits

Grid Dimensions:

N rows = first_digit + second_digit

M columns = first_digit + third_digit

Number Modification Rules:

If divisible by 5: subtract first digit

If divisible by 3: subtract second digit

Otherwise: add third digit

Output Format:

Numbers separated by spaces

New line after each row

M numbers per row

N total rows

For example, with input 132:

N = 1 + 3 = 4 rows

M = 1 + 2 = 3 columns

Creates 4x3 grid of modified numbers
'''