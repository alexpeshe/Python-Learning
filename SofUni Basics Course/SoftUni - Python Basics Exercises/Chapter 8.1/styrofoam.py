import math  # Import math module for ceiling function

# Input Section: Gathering all necessary data
budget = float(input())        # Available money for renovation
house_area = float(input())    # Total area of the house
windows = int(input())         # Number of windows
styrofoam = float(input())     # Area that one packet of styrofoam covers
styrofoam_price = float(input())  # Price per packet of styrofoam

# Calculate actual area needing coverage
# Subtract window areas (each window is 2.4 square units)
house_area = house_area - 2.4*windows

# Add 10% extra area for waste and overlaps
house_area = house_area + house_area*0.10

# Calculate number of packets needed
# Use ceiling function to round up (can't buy partial packets)
packets = math.ceil(house_area/styrofoam)

# Calculate total price
price = packets * styrofoam_price

# Calculate difference between budget and price
diff = abs(budget-price)

# Output Section: Display results based on budget comparison
if budget >= price:
    print(f"Spent :{price:.2f}")    # If enough budget, show spent amount
    print(f"Left :{diff:.2f}")      # And remaining money
else:
    print(f"Need more :{diff:.2f}") # If not enough budget, show needed amount

"""
Comprehensive Analysis
--------------------------------------------------------------------
Program Purpose
Calculates whether a given budget is sufficient for house insulation

Accounts for windows and extra material needs

Provides detailed cost breakdown

Key Components
Input Handling

Takes 5 different inputs

Converts strings to appropriate number types

Area Calculations

Subtracts window areas

Adds 10% extra for waste

Uses actual measurements

Cost Calculations

Calculates required packets

Determines total cost

Compares with budget

Output Formatting

Uses f-strings for formatting

Shows 2 decimal places

Provides different outputs based on budget

Key Points
Uses math.ceil() to round up packet numbers

Accounts for waste material (10%)

Considers window areas in calculations

Handles both sufficient and insufficient budget scenarios

Provides precise calculations to 2 decimal places
"""