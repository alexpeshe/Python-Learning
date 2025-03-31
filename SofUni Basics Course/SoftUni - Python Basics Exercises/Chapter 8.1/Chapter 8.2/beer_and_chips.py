#Beer and Chips Cost Calculator

"""
This program calculates the total cost of a snack purchase (beer and chips) and determines if the buyer has enough budget. Here's the code with detailed comments:
"""

import math  # Import the math module for rounding up

# Constant for the price of a single beer
BEER_PRICE = 1.20

# Get input from the user
name = input()  # Name of the buyer
budget = float(input())  # Available budget
count_beers = int(input())  # Number of beers to buy
count_chips = int(input())  # Number of chip packets to buy

# Calculate the cost of beers
beers_price = BEER_PRICE * count_beers

# Calculate the price of a single packet of chips (45% of the beer price)
chips_price = beers_price * 0.45

# Calculate the total price of all chip packets, rounding up to the nearest integer
all_chips_price = math.ceil(chips_price * count_chips)

# Calculate the total sum of the purchase
summ = beers_price + all_chips_price

# Calculate the absolute difference between the budget and the total sum
diff = abs(summ - budget)

# Check if the budget is sufficient and print the appropriate message
if budget >= summ:
    print(f"{name} bought a snack and has {diff:.2f} lv. left")
else:
    print(f"{name} needs {diff:.2f} more lv.")

#Concepts Learned

"""

Importing Modules: The program uses import math to access the ceil() function for rounding up.

Constants: BEER_PRICE is defined as a constant (conventionally in all caps) to store the fixed price of a beer.

User Input: The program takes multiple inputs from the user, including strings, floats, and integers.

Type Conversion: Input values are converted to appropriate types (float for budget, int for counts).

Arithmetic Operations: Various calculations are performed using multiplication and addition.

Rounding Up: math.ceil() is used to round up the chips price to the nearest integer.

Absolute Value: The abs() function is used to ensure a positive difference regardless of whether the budget is sufficient or not.

Conditional Statements: An if-else statement is used to determine which message to display based on the budget sufficiency.

String Formatting: F-strings are used with the :.2f format specifier to display monetary values with two decimal places.

Variable Naming: Descriptive variable names are used to make the code more readable (e.g., beers_price, all_chips_price).

Percentage Calculation: The program calculates 45% of the beer price for the chips price.

Comparison Operations: The >= operator is used to compare the budget with the total sum.

This program demonstrates basic input processing, arithmetic calculations, and conditional logic to solve a real-world problem of budget management for a simple purchase scenario."""