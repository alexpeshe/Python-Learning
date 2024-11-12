# SoftUni's improved by AI solution

# Import required modules (if needed)
import math
import random

# Get the number of elements to process
n = int(input())

# Initialize variables to store sums
leftSum = 0
rightSum = 0

# Process left side numbers
for i in range(0, n):
    numbersForLeftSide = float(input())
    leftSum += numbersForLeftSide

# Process right side numbers
for i in range(0, n):
    numbersForRightSide = float(input())
    rightSum += numbersForRightSide

# Compare sums and print appropriate message
if (leftSum == rightSum):
    print("Yes, sum = %d" % leftSum)
else:
    diff = abs(leftSum - rightSum)
    print("No, diff = %d" % diff)





# lesft_and_right_sum.py two for loops solution

'''
n = int(input())
left_sum = 0
right_sum = 0

for number in range(0, n):
    current_num = int(input())
    left_sum += current_num

for number in range(0, n):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print("Yes, sum = " + str(right_sum))
else:
    diff = abs(left_sum - right_sum)
    print("No, diff = " + str(diff))
'''
