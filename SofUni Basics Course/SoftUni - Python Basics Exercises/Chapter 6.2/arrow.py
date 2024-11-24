# Read the input: an odd integer n
n = int(input())

# Calculate the number of outer dots for the first row
out_dots = (n - 1) // 2  # Outer dots are (n-1)/2 for symmetry

# Print the first row of the arrow (the topmost row)
# This row has outer dots, followed by n hashes, followed by outer dots
print('.' * out_dots + '#' * n + '.' * out_dots)

# Calculate the number of inner dots for the body of the upper part
in_dots = n - 2  # Inner dots start at n-2 and remain constant in this section

# Loop to print the body of the upper part of the arrow
# Each row has constant outer dots, one hash, inner dots, another hash, and outer dots
for row in range(n - 2):  # Loop runs n-2 times for the upper body rows
    print('.' * out_dots + '#' + '.' * in_dots + '#' + '.' * out_dots)

# Print the middle part of the arrow
# The middle row has (out_dots + 1) hashes on both sides and inner dots in between
print('#' * (out_dots + 1) + '.' * in_dots + '#' * (out_dots + 1))

# Update variables for the lower part of the arrow
inner_dots = n - 3  # Inner dots start at n-3 and decrease by 2 each row
outer_dots = out_dots + 1  # Outer dots start at out_dots+1 and increase by 1 each row

# Loop to print the lower part of the arrow (except for the last row)
for row in range(n - 2):  # Loop runs n-2 times for rows below the middle part
    if inner_dots < 0:  # Stop when inner dots become negative (last row is handled separately)
        break
    # Each row has increasing outer dots, one hash, decreasing inner dots, another hash, and outer dots again
    print('.' * outer_dots + '#' + '.' * inner_dots + '#' + '.' * outer_dots)
    outer_dots += 1      # Increment outer dots by 1 for each subsequent row
    inner_dots -= 2      # Decrement inner dots by 2 for each subsequent row

# Print the last row of the arrow
# The last row has only one hash surrounded by all outer dots on both sides
print('.' * outer_dots + '#' + '.' * outer_dots)

