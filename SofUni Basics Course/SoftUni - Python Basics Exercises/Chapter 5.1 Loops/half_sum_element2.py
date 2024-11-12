# Get the number of integers
n = int(input())

# Initialize variables
total_sum = 0
max_num = 0
numbers = []  # We'll store the numbers in a list to avoid double input

# Read numbers and calculate sum and maximum
for i in range(n):
    num = int(input())
    numbers.append(num)  # Store the number
    total_sum += num
    if num > max_num:
        max_num = num

# Check if any number equals half the sum
found_solution = False
for num in numbers:  # Use stored numbers instead of asking for input again
    if num * 2 == total_sum:
        print("YES")
        print('Sum = ', num)
        found_solution = True
        break

# If no solution was found
if not found_solution:
    difference = abs(2 * max_num - total_sum)
    print("NO")
    print('No diff =', difference)