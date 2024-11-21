n = int(input())

# This version starts the row from 1 and goes up to n (inclusive)
for row in range(1, n + 1):
    # Multiply '$ ' by the current row number
    # This creates a pattern where each row increases in width
    print('$ '* row)

'''
Alternative solution
# This version starts the row from 0 and goes up to n-1
for row in range(0, n):
    # Add 1 to the row number when multiplying
    # This achieves the same result as the first version
    print('$ '* (row+1))
'''

'''Furthermore, Key Differences Explained:

First version: range(1, n + 1)

Directly uses row number
Starts from 1
Goes up to n

Alternative version: range(0, n)

Uses row+1 to compensate for starting at 0
Starts from 0
Goes up to n-1

'''