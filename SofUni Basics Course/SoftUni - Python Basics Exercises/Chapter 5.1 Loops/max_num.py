# Get the number of inputs from the user
n = int(input())

# Initialize the maximum number to 0
max_num = 0

# Loop n times to get n inputs from the user
for number in range(0, n):
    # Get an input number from the user and convert it to an integer
    input_number = int(input())
    
    # If the input number is greater than the current maximum,
    # update the maximum
    if input_number > max_num:
        max_num = input_number

# After all inputs are processed, print the maximum number
print(max_num)

''' 
SoftUni's original solution

n = int(input())
max_number = 9223372036854775807
for number in range(0, n):
    input_number = int(input())
    if input_number › max_number:
        max_number=input_number
print(max_number) 
'''

'''
2nd alternative solution 

n = int(input('n = '))
max = -10000000000000

for i in range(n):
    num = int (input())
    if num › max:
        max = num

print('max = ' + str (max))

'''