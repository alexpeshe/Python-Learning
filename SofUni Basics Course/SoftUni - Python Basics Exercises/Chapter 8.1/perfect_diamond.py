# This program draws a diamond pattern using asterisks (*) and underscores (_)
# The size of the diamond is determined by user input 'n'

# Get the size of the diamond from user input
n = int(input())  # n determines the number of rows in the upper half of the diamond

# The issue with the original code is in the spacing calculation.
# For a diamond, spaces should decrease as we approach the middle row
# and increase as we move away from it.

# Upper half of the diamond (including the middle row)
for i in range(1, n + 1):  # i represents the current row number, starting from 1 up to n
    # Print spaces followed by the first asterisk
    # We need (n-i) spaces to create a proper diamond shape
    print(' ' * (n - i) + '*', end='')  # end='' prevents a newline so we can continue on the same line

    # This loop adds pairs of underscore and asterisk for all rows except the first
    # j is just a counter variable that goes from 0 to i-2
    for j in range(0, i - 1):
        print('_*', end='')  # Print an underscore followed by an asterisk

    # End the current row with a newline
    #print()

# Lower half of the diamond (excluding the middle row)
# reversed() function creates an iterator that accesses the sequence in reverse order
# Here it makes i go from n-1 down to 1
for i in reversed(range(1, n)):  # i represents the current row number, going from n-1 down to 1
    # Print spaces followed by the first asterisk
    # We need (n-i) spaces to create a proper diamond shape
    print(' ' * (n - i) + '*', end='')

    # This loop adds pairs of underscore and asterisk
    # Same logic as in the upper half
    for j in range(0, i - 1):
        print('_*', end='')

    # End the current row with a newline
    #print()

'''
This code creates a diamond pattern, but there might be an issue with the spacing formula ' '*(n*i). Let me explain the key elements:

Variables explanation:

i: Represents the current row number in each half of the diamond

j: A counter variable used to add the correct number of "_*" pairs

reversed() function:

reversed(range(1, n)) creates an iterator that produces the values from range(1, n) in reverse order

For example, if n=5, this produces the sequence: 4, 3, 2, 1

This is used to create the lower half of the diamond by going from n-1 down to 1

Potential issue:

The spacing formula ' '*(n*i) might produce too many spaces

For a typical diamond pattern, spaces should decrease as you approach the middle row

If you're not getting the expected diamond shape, you might want to reconsider the spacing formula. A more typical approach would be something like ' '*(n-i) for the upper half and ' '*(n-i) for the lower half.'''