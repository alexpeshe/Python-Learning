# Get the number of inputs from the user
n = int(input())

# Initialize the maximum number to 0
min_num = 100000000000

# Loop n times to get n inputs from the user
for number in range(0, n):
    # Get an input number from the user and convert it to an integer
    input_number = int(input())
    
    # If the input number is greater than the current maximum,
    # update the maximum
    if input_number < min_num:
        min_num = input_number

# After all inputs are processed, print the maximum number
print(min_num)
