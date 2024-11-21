# Input the size of the house (number of rows)
n = int(input())

# Calculate the size of the roof (triangular part at the top)
roof = n//2

# Calculate the total space between the side walls
space = 2*n - 2

# Calculate the number of dashes in the middle of the house
dash = 2*n - 4 - (n//2)*2

# Print the top of the house (roof)
# Consists of: 
# - Left side slash '/'
# - Roof peaks '^'
# - Right side backslash '\'
# - Middle dashes '_'
# - Another roof section
print('/' + '^'*roof + '\\' + '_'*dash +  '/' + '^'*roof + '\\')

# Create the body of the house
for row in range(0, n-2):
    # Special case for the bottom row of the body
    if row == n-3:
        # Print a row with some spacing and a dash in the middle
        print('|' + ' '*(n//2) + ' ' + '-'*dash + ' ' + ' '*(n//2) + '|')
    else:
        # Print standard rows with side walls and empty space
        print('|' + ' '*space + '|')

'''# Create the body of the house
for row in range(0, n-2):
    # Special case for the bottom row of the body
    if row == n-3:
        # Print a row with some spacing in the middle
        print('|' + ' '*(n//2) + ' ' + ' '*dash + ' ' + ' '*(n//2) + '|')
    else:
        # Print standard rows with side walls and empty space
        print('|' + ' '*space + '|')'''

# Print the bottom of the house
# Similar to the top, but with inverted slashes and underscores
print('\\' + '_'*roof + '/' + ' '*dash +  '\\' + '_'*roof + '/')

'''
Key points about this code:

It creates an ASCII art house
The size of the house is determined by the input n
The house has a triangular roof, side walls, and a base
The dimensions are calculated dynamically based on the input size
Different rows are printed with varying amounts of spacing
The house is symmetrical
The code uses integer division (//), string multiplication for repeating characters, and carefully calculated spacing to create the house shape.

'''