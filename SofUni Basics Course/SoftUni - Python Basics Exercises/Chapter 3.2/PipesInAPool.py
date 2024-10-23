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
    pool_fill_percentage = math.trunc(pool_fill_percentage)
    pipe1_percentage = math.trunc(pipe1_percentage)
    pipe2_percentage = math.trunc(pipe2_percentage)

    #  print(The pool is [0]% full. Pipe 1: [1]%. Pipe 2: [2]%." .format (

    print(f"The pool is {pool_fill_percentage}% full. Pipe 1: {pipe1_percentage}%. Pipe 2: {pipe2_percentage}%.")
else:
    # Pool is overflowing
    overflow = W - V  # Calculate how much water overflowed
    print(f"For {H} hours the pool overflows with {overflow:.1f} liters.")



'''
Step-by-Step Breakdown
Input Values:

V: Total pool capacity in liters.
P1: Flow rate of the first pipe (liters/hour).
P2: Flow rate of the second pipe (liters/hour).
H: Number of hours the pipes are left running.
Total Water Calculation:

Total Water=(P1+P2)×H

W is how much water both pipes combined pour into the pool over H hours.
Checking if Water Fits into the Pool:

If W <= V:
Calculate percentages contributed by each pipe and the total fill percentage of the pool.

Else:
Calculate how much water is in excess (overflow).
Final Tips for Handling If-Else Logic
Use simple steps to break down the logic.
Write out each condition one at a time before coding it.
Don’t hesitate to use print() statements in between to see what’s happening at each step. For example:

print(f"Total Water: {W} liters, Pool Capacity: {V} liters")

This way, you can visualize your calculations and spot where things might be going wrong.

You’ve got this! Each time you tackle these logical problems, you’re building a stronger foundation, and soon, these “simple if-else” will become second nature! 💪
'''

