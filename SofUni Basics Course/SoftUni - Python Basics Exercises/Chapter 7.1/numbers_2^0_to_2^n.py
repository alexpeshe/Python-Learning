# Prompt the user to input a number and convert it to an integer
n = int(input())

# Loop through numbers from 0 to n (inclusive)
# range(0, n+1) creates a sequence: 0, 1, 2, ..., n
for num in range(0, n+1):
    # Calculate 2 raised to the power of the current number
    # pow(2, num) is equivalent to 2**num
    # This calculates powers of 2: 2^0, 2^1, 2^2, ..., 2^n
    a = pow(2, num)
    
    # Print the current number (not the calculated power)
    # This will print: 0, 1, 2, ..., n
    print(num)

# Example:
# If n = 4, the output will be:
# 0
# 1
# 2
# 3
# 4

# Note: The calculated power (a) is not used or printed
# So a would be: 1, 2, 4, 8, 16 respectively

'''
Key points:

range(0, n+1) creates a sequence starting from 0 up to and including n
pow(2, num) calculates 2 raised to the power of the current number
print(num) outputs the current number in the sequence
The power calculation is done but not used in this specific example
'''  # Removed the comment about the prompt, as it's not necessary. The code already shows

'''
alternative softuni solution

num = 1

for num in range(0, n+1):
    print(num)
    num = num * 2

'''