# Prompt the user to input a number and convert it to an integer
n = int(input())

# Start a reverse loop from n down to 0 (inclusive)
# range(start, stop, step) parameters:
# - start: n (beginning value, the number entered by the user)
# - stop: -1 (the loop will go down to 0, so stop is set to -1 to include 0)
# - step: -1 (negative step means counting down instead of up)
for i in range(n, -1, -1):
    # Print each number in descending order
    # This will print: n, n-1, n-2, ..., 2, 1, 0
    print(i)

# Example:
# If n = 5, the output will be:
# 5
# 4
# 3
# 2
# 1
# 0

'''
Key points:

range(n, -1, -1) creates a sequence that:
Starts at n
Stops before -1 (which means it includes 0)
Decrements by 1 in each iteration
This effectively prints all numbers from n down to 0 in descending order
'''