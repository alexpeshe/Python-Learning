def print_diamond(n):
    # Upper half of diamond (including middle line)
    # Iterate from 0 to n-1
    for i in range(n):
        # Calculate and print leading spaces
        # Spaces decrease as we move down the diamond
        # Formula: (n - i - 1) ensures right alignment
        # Example: 
        # When n=6, first row has 5 spaces
        # Last row has 0 spaces
        print(' ' * (n - i - 1), end='')
        
        # Calculate and print stars
        # Formula: (2 * i + 1) creates odd number of stars
        # Increases from 1 to (2n-1)
        # Example progression:
        # i=0: 1 star
        # i=1: 3 stars
        # i=2: 5 stars
        # ...and so on
        print('*' * (2 * i + 1))
    
    # Lower half of diamond
    # Iterate from (n-2) down to 0 in reverse
    # Start from n-2 to avoid repeating the middle line
    for i in range(n - 2, -1, -1):
        # Calculate and print leading spaces
        # Similar to upper half, but in reverse
        # Spaces increase as we move down
        print(' ' * (n - i - 1), end='')
        
        # Calculate and print stars
        # Decreasing number of stars
        print('*' * (2 * i + 1))

# Example usage with diamond size of 6
print_diamond(6)

# Detailed visual breakdown for n=6:
# Spaces | Stars | Row Description
#   5    |   1   | Top point
#   4    |   3   | 
#   3    |   5   | 
#   2    |   7   | Middle line
#   1    |   5   | 
#   0    |   3   | 
#   1    |   1   | Bottom point

# Resulting pattern would look like:
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *