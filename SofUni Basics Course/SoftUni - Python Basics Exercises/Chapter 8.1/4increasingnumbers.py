# This program finds and prints all possible combinations of 4 distinct integers 
# within a given range [a, b] in ascending order.

# Read the lower bound of the range from user input
a = int(input())
# Read the upper bound of the range from user input
b = int(input())

# Initialize a counter to keep track of how many combinations are found
count = 0

# First loop: i takes values from a to b (inclusive)
for i in range(a, b+1):
    # Second loop: j takes values from i+1 to b (inclusive)
    # This ensures j > i (first number is smaller than second)
    for j in range(i+1, b+1):
        # Third loop: k takes values from j+1 to b (inclusive)
        # This ensures k > j > i (third number is larger than second and first)
        for k in range(j+1, b+1):
            # Fourth loop: l takes values from k+1 to b (inclusive)
            # This ensures l > k > j > i (all numbers in ascending order)
            for l in range(k+1, b+1):
                # Print the current combination of 4 distinct integers
                print('%d %d %d %d' % (i, j, k, l))
                # Increment the counter for each valid combination found
                count+=1

# If no combinations were found (count is still 0)
if count == 0:
    # Print "No" to indicate no valid combinations exist
    print('No')

'''
This code generates all possible combinations of 4 distinct integers within the range [a, b] where each combination is in ascending order. Here's what it does:

It uses nested loops to systematically generate all possible combinations where i < j < k < l.

The range for each variable is carefully defined to ensure this ordering:

i starts from a and goes up to b

j starts from i+1 (ensuring j > i)

k starts from j+1 (ensuring k > j)

l starts from k+1 (ensuring l > k)

For each valid combination, it prints the four numbers and increments a counter.

If no valid combinations are found (which happens when b-a < 3, since we need at least 4 distinct integers), it prints "No".

For example, if a=1 and b=5, it will print combinations like "1 2 3 4", "1 2 3 5", "1 2 4 5", etc.'''