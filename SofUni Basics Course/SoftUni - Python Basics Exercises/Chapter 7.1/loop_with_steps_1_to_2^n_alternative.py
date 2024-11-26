# Prompt the user to input a number and convert it to an integer
n = int(input())

# Loop through numbers from 1 to n (inclusive)
# range(1, n+1) creates a sequence: 1, 2, 3, ..., n
for i in range(1, n+1):
    # Calculate the square of the current number
    # pow(i, 2) is equivalent to i**2
    # This calculates squares: 1^2, 2^2, 3^2, ..., n^2
    print(pow(i, 2))

# Example:
# If n = 5, the output will be:
# 1  (1^2)
# 4  (2^2)
# 9  (3^2)
# 16 (4^2)
# 25 (5^2)

# Note: 
# - pow() is a built-in Python function for exponentiation
# - The comment in Bulgarian translates to: 
#   "pow is a built-in Python function that raises ⬤
#   to the power of ⬤"

# pow e вградена функция на python, която вдига степените 

'''
Key points:

range(1, n+1) creates a sequence starting from 1 up to and including n
pow(i, 2) calculates the square of the current number
print() immediately outputs the squared value
The loop calculates and prints the squares of numbers from 1 to n
'''