# Initialize the variable 'gauss' to 0
gauss = 0

# Start a loop that will run 100 times, with 'i' taking values from 1 to 100
for i in range(1, 101):
    # This condition is always true for this loop, so it's redundant
    if i>=1:
        # Calculate the sum of integers from 1 to i using Gauss's formula
        # i*(i+1)/2 gives the sum of all integers from 1 to i
        gauss = i*(i+1)/2
        
        # Print the current sum
        # This will show the progression of sums for each value of i from 1 to 100
        print(gauss)