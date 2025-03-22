# For loops
# for item in sequence(n,-1):
    # code block

for i in range(0,10):
    if i == 7:
        break
    if(i == 2):
        continue
        print(i, end='')

'''
Notes:

The key difference between if and elif:

Example one:

for i in range(0,10):
    if i == 7:           # First condition is checked independently
        break
    if i == 2:           # Second condition is checked independently
        continue
    print(i, end='')
    
Example 2:

for i in range(0,10):
    if i == 7:           # First condition is checked
        break
    elif i == 2:         # Only checked if first condition is False
        continue
    print(i, end='')

    
Key Differences:

With separate if statements:

Each condition is checked independently

Both conditions could be True (though not in this specific case)

More flexible but might be less efficient

With if-elif:

Conditions are checked in sequence

Once one condition is True, others are skipped

More efficient but more restrictive

In this specific example:

Both would actually work the same because:

When i=7, the break happens

When i=2, the continue happens

The conditions can't both be true at the same time

However, using separate if statements is more appropriate here because:

The conditions are independent of each other

We want both conditions to be checked separately

They serve different purposes (breaking vs continuing)

------------------------------------------------------------------------------------
Example where it matters:

# Using if statements
x = 10
if x > 5:    # This runs
    print("Above 5")
if x > 8:    # This also runs
    print("Above 8")
# Output: Above 5
#         Above 8

# Using if-elif
x = 10
if x > 5:    # This runs
    print("Above 5")
elif x > 8:  # This never runs because first condition was True
    print("Above 8")
# Output: Above 5

    '''