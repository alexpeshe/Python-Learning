# Get the number of integers
n = int(input())  # First input: 7

# Initialize variables

total_sum = 0
max_num = 0

# First pass: calculate sum and find maximum
for i in range(n):
    num = int(input())  # Will read next 7 numbers one by one:
    # 3, 4, 1, 1, 2, 12, 1
    total_sum += num
    if num > max_num:
        max_num = num

# After first loop:
# Example: total_sum will be 24 (3+4+1+1+2+12+1)
# max_num will be 12

found_solution = False

# Second pass: check each number
for i in range(n):
    num = int(input())  # Will read the same 7 numbers again
    if num * 2 == total_sum:  # Is any number equal to 12 (half of 24)?
        print("YES")
        print(num)
        found_solution = True
        break

# Since 12 * 2 = 24 (total_sum)
# Program will print:
# YES
# 12


    '''
    
? question how do I know if range is just n or, 1, n, or even 1, n+1


Great question! Understanding how to use the range() function is crucial. Let me explain the different ways to use range():

range(n):

This creates a sequence from 0 to n-1.
Example: If n = 5, this gives you 0, 1, 2, 3, 4
range(1, n+1):

This creates a sequence from 1 to n.
Example: If n = 5, this gives you 1, 2, 3, 4, 5
range(1, n):

This creates a sequence from 1 to n-1.
Example: If n = 5, this gives you 1, 2, 3, 4
For this specific problem:

We use range(n) because:
We want to loop exactly n times.
We don't actually use the loop variable i in our calculations.
In Python, it's conventional to start counting from 0.
So, for i in range(n): is perfect here. It will loop exactly n times, which is what we need to read n numbers from the input.

Remember:

If you need to count from 1 to n, use range(1, n+1)
If you just need to do something n times and don't care about the actual numbers, use range(n)
In this problem, we're just doing something n times (reading n numbers), so range(n) is the most appropriate choice.'''