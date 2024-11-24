# Input the size of the axe
n = int(input())

# Calculate the total width of the axe pattern
width = 5*n  # Total width is 5 times the input size

# Initial positioning of dashes
left_dashes = 3*n     # Starting length of left side dashes
middle_dashes = 0     # Initial middle section (empty)
# Calculate right side dashes to complete the total width
right_dashes = width - left_dashes - middle_dashes - 2  # Subtract 2 for the asterisk separators

# First section: Creating the top expanding part of the axe head
for i in range(n):
    # Print a row with left dashes, middle dashes, and right dashes
    # Separated by asterisks
    print("{0}*{1}*{2}".format('-'*left_dashes,'-'*middle_dashes,'-'*right_dashes))
    
    # Expand the middle section
    middle_dashes += 1  # Increase middle dashes
    right_dashes -= 1   # Decrease right dashes to maintain overall width

# Adjust parameters after first section
middle_dashes -= 1     # Reduce middle dashes by 1
left_dashes += 1       # Increase left dashes
right_dashes += 1      # Increase right dashes

# Calculate the height of the axe handle
axe_height = int(n/2)

# Second section: Creating the solid part of the axe head
for i in range(axe_height):
     # Print rows with asterisks on the left side
     print("{0}*{1}*{2}".format('*'*left_dashes,'-'*middle_dashes,'-'*right_dashes))
     
     # Reduce left and right dashes
     left_dashes -= 1
     right_dashes -= 1

# Third section: Creating the bottom tapering part of the axe head
for i in range(axe_height -1):
     # Print rows with dashes, gradually expanding middle
     print("{0}*{1}*{2}".format('-'*left_dashes,'-'*middle_dashes,'-'*right_dashes))
     
     # Expand middle, reduce left and right
     middle_dashes += 2
     left_dashes -= 1
     right_dashes -= 1

# Final row: Bottom of the axe with a filled middle section
print("{0}*{1}*{2}".format('-'*left_dashes,'*'*middle_dashes,'-'*right_dashes))


'''
n = int(input())

width = 5*n
left_dashes = 3*n
middle_dashes = 0
right_dashes = width - left_dashes - middle_dashes - 2

# print("{0}**{1}".format('-'*left_dashes,'-'*right_dashes))

for i in range(n):
    print("{0}*{1}*{2}".format('-'*left_dashes,'-'*middle_dashes,'-'*right_dashes))
    middle_dashes += 1
    right_dashes -= 1

middle_dashes -=1
left_dashes +=1
right_dashes +=1

axe_height = int(n/2)

for i in range(axe_height):
     print("{0}*{1}*{2}".format('*'*left_dashes,'-'*middle_dashes,'-'*right_dashes))
     left_dashes -= 1
     right_dashes -= 1

for i in range(axe_height -1):
     print("{0}*{1}*{2}".format('-'*left_dashes,'-'*middle_dashes,'-'*right_dashes))
     middle_dashes += 2
     left_dashes -= 1
     right_dashes -= 1

print("{0}*{1}*{2}".format('-'*left_dashes,'*'*middle_dashes,'-'*right_dashes))
'''

'''
Formatting explained 
--------------------
Example
---------
print("{0}*{1}*{2}".format('*'*left_dashes, '-'*middle_dashes, '-'*right_dashes))
--------------------------------------------------------------------------------

String Template "{0}*{1}*{2}":

{0}: First placeholder (left side)
*: Literal asterisk separator
{1}: Second placeholder (middle section)
*: Another literal asterisk separator
{2}: Third placeholder (right side)
.format() Method Arguments:

First argument '*'*left_dashes: Repeats * left_dashes times
Second argument '-'*middle_dashes: Repeats - middle_dashes times
Third argument '-'*right_dashes: Repeats - right_dashes times

--------------------------------------------------------------------------------

Further examples

# If left_dashes = 3, middle_dashes = 2, right_dashes = 4
print("{0}*{1}*{2}".format('*'*3, '-'*2, '-'*4))
# Output: ****--*----

# If left_dashes = 2, middle_dashes = 3, right_dashes = 1
print("{0}*{1}*{2}".format('*'*2, '-'*3, '-'*1))
# Output: ***---*-

--------------------------------------------------------------------------------

Alternative modern Python syntax:

# f-string (Python 3.6+)
print(f"{'*'*left_dashes}*{'-'*middle_dashes}*{'-'*right_dashes}")

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

Key points:

'*'*n creates a string of n asterisks
'-'*n creates a string of n dashes
The .format() method replaces {0}, {1}, {2} with the corresponding arguments
The f-string syntax is a more modern alternative to .format() for string formatting
--------------------------------------------------------------------------------
'''