n = int(input())

print("*"* n)

for i in range(1, n-1):
    print("*" + " " *(n-2) + "*")

print("*"* n)

''' 
The for loop does the following:

This starts a loop that will run n-2 times (from 1 to n-2 inclusive). 
This loop will create the middle rows of the square.


For each iteration of the loop, this line prints:

An asterisk "*" at the beginning
n-2 spaces in the middle (because we need 2 less spaces than n to account for the asterisks at the start and end)
Another asterisk "*" at the end
'''