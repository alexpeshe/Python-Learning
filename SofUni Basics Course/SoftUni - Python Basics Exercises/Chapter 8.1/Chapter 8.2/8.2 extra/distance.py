# My Solution

# Read input values
initial_speed = int(input())
first_time_min = int(input())
second_time_min = int(input())
third_time_min = int(input())

# Convert minutes to hours
first_time_hours = first_time_min / 60
second_time_hours = second_time_min / 60
third_time_hours = third_time_min / 60

# Calculate distances for each segment
# First segment - initial speed
first_distance = initial_speed * first_time_hours

# Second segment - speed increased by 10%
second_speed = initial_speed * 1.1  # Same as initial_speed + initial_speed * 0.1
second_distance = second_speed * second_time_hours

# Third segment - speed decreased by 5% from the increased speed
third_speed = second_speed * 0.95  # Same as second_speed - second_speed * 0.05
third_distance = third_speed * third_time_hours

# Calculate total distance
total_distance = first_distance + second_distance + third_distance

# Format and display the result
print(f"{total_distance:.2f}")

'''
Improving Your Problem-Solving Logic:

For problems like the distance calculation example, try this structured approach:

1. Break Down the Problem Before Coding
Before writing any code, break the problem into clear steps on paper:

What are the inputs? (Initial speed, 3 time intervals)

What are the calculations for each segment? (Distance = speed × time)

How does the speed change between segments? (First +10%, then -5%)

What's the expected output format? (Distance with 2 decimal places)

2. Use Pseudocode
Write out the logic in plain language first:

Read inputs
Convert first time to hours
Calculate first distance using initial speed
Calculate new speed (10% increase)
Convert second time to hours
Calculate second distance using increased speed
Calculate final speed (5% decrease from increased speed)
Convert third time to hours
Calculate third distance
Sum all distances
Format and display result

3. Test With Simple Examples
Work through the example data manually before coding to verify your understanding.

4. Identify Formula Patterns
In your original solution, the issue was with understanding how to calculate percentage changes. Remember:

Increase by X%: original + (original × X/100)

Decrease by X%: original - (original × X/100)

5. Implement Step by Step
Code one section at a time, testing as you go.

For University Programming Tasks
University programming tasks often require:

Careful reading - extract all requirements and constraints

Mathematical precision - understand the exact formulas needed

Edge case handling - consider all possible input scenarios

Attention to detail - follow output format requirements exactly

Don't be discouraged by these challenges. The ability to break down complex problems is a skill that improves with practice. Each problem you work through, even if you initially struggle, builds your problem-solving toolkit.'''

# SUni's
# Read input
starting_speed = int(input())
first_int = int(input())
second_int = int(input())
final_int = int(input())

min_per_hour = 60

# First interval - initial speed
first_interval_hours = first_int / min_per_hour
first_distance = starting_speed * first_interval_hours

# Second interval - speed increased by 10%
speed_after_increase = starting_speed + (starting_speed * 10 / 100)
second_int_hours = second_int / min_per_hour
second_distance = speed_after_increase * second_int_hours

# Third interval - speed decreased by 5% from the increased speed
speed_after_decrease = speed_after_increase - (speed_after_increase * 5 / 100)
third_int_hours = final_int / min_per_hour
third_distance = speed_after_decrease * third_int_hours

# Calculate total distance
final_distance = first_distance + second_distance + third_distance

# Format and print result
final_result = "{:.2f}".format(final_distance)
print(final_result)


