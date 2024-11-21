# Prompt the user to input the size of the rectangle
# The input will determine the width and height of the rectangle
n = int(input())

# Print the top border of the rectangle
# '+' at the start and end, with '-' filling the middle
# n-2 ensures the inner width is correct
# Example: if n=5, this prints: +---+
print('+ ' + ('- ' * (n-2)) + '+' )

# Create the middle rows of the rectangle
# The loop runs n-2 times to create the inner bo of the rectangle
# This ensures the rectangle has the correct height
for row in range(0, n-2):
    # Print each row with '|' at the sides and '-' in the middle
    # n-2 ensures the inner width is consistent
    # Example: if n=5, this prints: |---| for each row
    print('| ' + ('- ' * (n-2)) + '|' )

# Print the bottom border of the rectangle
# Same logic as the top border
# Completes the rectangle
print('+ ' + ('- ' * (n-2)) + '+' )

# Visual breakdown of how it works:
# For n = 5, the output would look like:
# +---+
# |---| 
# |---| 
# +---+