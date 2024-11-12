# Get the number of elements for each side
n = int(input())

# Initialize variables to store the sum of left and right sides
left_sum = 0
right_sum = 0

# Loop to process 2n numbers (n for left side, n for right side)
for number in range(0, n*2):
    # Get the current number from user input
    current_num = int(input())
    
    # Add numbers to left_sum if they're in the first half of inputs
    if number < n:
        left_sum += current_num
    # Add numbers to right_sum if they're in the second half of inputs
    elif number >= n:
        right_sum += current_num

# Compare the sums and output the result
if left_sum == right_sum:
    # If sums are equal, print "Yes" and the sum
    print("Yes, sum = " + str(right_sum))
else:
    # If sums are not equal, calculate the difference and print "No"
    diff = abs(left_sum - right_sum)
    print("No, diff = " + str(diff))




'''n = int(input())
left_sum = 0
right_sum = 0

for number in range(0, n*2):
    current_num = int(input())
    if number < n:
        left_sum += current_num
    elif number >= n:
        right_sum += current_num
    
if left_sum == right_sum:
    print("Yes, sum = " + str(right_sum))
else:
    diff = abs(left_sum - right_sum)
    print("No, diff = " + str(diff))'''
