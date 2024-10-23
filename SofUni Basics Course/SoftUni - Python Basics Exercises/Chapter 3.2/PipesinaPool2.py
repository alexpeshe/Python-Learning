import math

# Reading input values
V = int(input())  # Volume of the pool
P1 = int(input())  # Flow rate of the first pipe
P2 = int(input())  # Flow rate of the second pipe
H = float(input())  # Hours the worker is absent

# Calculating the total water from both pipes after H hours
W = (P1 + P2) * H

# Checking if the water fits within the pool's volume
if W <= V:
    # Pool is not overflowing
    pool_fill_percentage = (W / V) * 100  # Pool fill percentage
    pipe1_percentage = (P1 * H / V) * 100  # Contribution of pipe 1
    pipe2_percentage = (P2 * H / V) * 100  # Contribution of pipe 2

    # Using math.trunc() to truncate the percentages without rounding
    print(f"The pool is {math.trunc(pool_fill_percentage)}% full. Pipe 1: {math.trunc(pipe1_percentage)}%. Pipe 2: {math.trunc(pipe2_percentage)}%.")

else:
    # Pool is overflowing
    overflow = W - V  # Calculate how much water overflowed
    print(f"For {H} hours the pool overflows with {overflow:.1f} liters.")

'''
Breaking Down the Code
Step 1: We gather all the inputs from the user.
Step 2: Calculate W, which is the total water filled in H hours.
Step 3: Use an if condition to check if the pool is overflowing:
If the total water (W) is less than or equal to V, we calculate how full the pool is in percentages.
If the pool is overflowing (W > V), we calculate the overflow.
Step 4: Output the results with formatted strings.
Why Use math.trunc?
The function math.trunc() ensures that the percentages are displayed as whole numbers. So, for example, 66.67% will become 66%, making it more readable.
Practice to Build Confidence!
I know conditionals can feel tricky at first. But once you break down the logic step-by-step, it gets much easier. I suggest testing this with different inputs to see how the code behaves. Focus on small successes to build momentum, and I’ll always be here to help guide you through it! 😄

Let me know what part you’d like to go over again, and we can tackle it together!
'''