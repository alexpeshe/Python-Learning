# Prompt the user to input a number and convert it to an integer
n = int(input())

# Initialize the first result value to 1
# This will be the starting point of our sequence
result = 1

# Loop through odd numbers from 1 to n
# range(1, n+1, 2) generates: 1, 3, 5, 7, ...
for num in range(1, n+1, 2):
    # Print the current result value
    print(result)
    
    # Update the result using the formula: result = result * 2 + 1
    # This creates a sequence with a specific pattern
    # Each iteration doubles the previous result and adds 1
    result = result*2+1
    
    # Break the loop if the result exceeds the input number n
    # This prevents printing numbers larger than the input
    if result > n:
        break

# Logic Breakdown:
# 1. Start with result = 1
# 2. First iteration: 
#    - Print 1
#    - New result = 1*2+1 = 3
# 3. Next iteration:
#    - Print 3
#    - New result = 3*2+1 = 7
# 4. Continues until result > n

# Example:
# If n = 10
# Output will be:
# 1
# 3
# 7

'''
Key Points:

Sequence Generation
Uses a specific formula: result = result * 2 + 1
Creates a sequence: 1, 3, 7, 15, 31, ...
Iteration Strategy
range(1, n+1, 2) ensures only odd numbers are used as loop indices
Provides a structured way to control iterations
Conditional Termination
if result > n: break prevents exceeding the input number
Dynamically stops the sequence generation
Pattern Characteristics
Each number is derived from the previous one
Follows a geometric progression with a twist
Doubles the previous value and adds 1
Mathematical Pattern:

1st term: 1
2nd term: 1*2+1 = 3
3rd term: 3*2+1 = 7
4th term: 7*2+1 = 15
And so on...


Skill Demonstration:

Dynamic sequence generation
Controlled iteration
Conditional loop termination
Mathematical sequence manipulation
Recommended Exploration:

Experiment with different starting values
Modify the formula
Add more complex conditions
Understand the underlying mathematical logic

'''

'''
SoftUni's alternative solution:

n = int (input ())
num = 1
for i in range(0, n + 1, 2):
    print (num)
    num = num * 2 * 2
    '''