# My solution:

flower = input().lower()
flower_quantity = int(input())
season = input().lower()

harvest = 0
honey = 0

# Calculate base harvest
if season == 'Spring':
    if flower == 'Sunflower':
        harvest = flower_quantity * 10
    elif flower == 'Daisy':
        harvest = flower_quantity * 12
    elif flower == 'Lavender':
        harvest = flower_quantity * 12
    elif flower == 'Mint':
        harvest = flower_quantity * 10
elif season == 'Summer':
    if flower == 'Sunflower':
        harvest = flower_quantity * 8
    elif flower == 'Daisy':
        harvest = flower_quantity * 8
    elif flower == 'Lavender':
        harvest = flower_quantity * 8
    elif flower == 'Mint':
        harvest = flower_quantity * 12
elif season == 'Autumn':
    if flower == 'Sunflower':
        harvest = flower_quantity * 12
    elif flower == 'Daisy':
        harvest = flower_quantity * 6
    elif flower == 'Lavender':
        harvest = flower_quantity * 6
    elif flower == 'Mint':
        harvest = flower_quantity * 6

# Apply seasonal bonuses
honey = harvest  # Start with base harvest

"""
The approach of setting honey = harvest first and then applying bonuses is better than your original approach for a few key reasons:

Clarity and Logic Flow:

Starting with honey = harvest establishes a clear baseline before applying any modifications

It follows the logical sequence of the problem: first calculate the base harvest, then apply the seasonal adjustments

Avoiding Logic Errors:

Your original approach had a fundamental issue: you were setting honey directly with the bonus already applied in each condition

This led to problems like the Spring condition applying a 5% reduction (honey = harvest * 0.95) which doesn't match the problem requirements

Handling Special Cases:

In your original code, you had two separate if conditions for Spring, with the second one never being reached

The corrected approach handles all seasonal bonuses in a single, clear section

Maintainability:

If the problem requirements change (e.g., new bonuses are added), the corrected structure makes it much easier to update the code

The separation between base calculation and bonus application makes the code's purpose clearer

The corrected approach follows a "calculate base value, then apply modifiers" pattern, which is generally more robust and less error-prone than trying to calculate the final value in one step, especially when there are multiple potential modifiers that might apply."""

if season == 'Summer':
    honey *= 1.10  # 10% more honey in Summer
elif season == 'Autumn':
    honey *= 0.95  # 5% less honey in Autumn
elif season == 'Spring':
    if flower == 'Daisy' or flower == 'Mint':
        honey *= 1.10  # 10% more for Daisy and Mint in Spring

# Alternative AI's:

"""
# Apply seasonal bonuses
if season == 'Summer':
    honey = honey * 1.10  # 10% more honey in Summer
elif season == 'Autumn':
    honey = honey * 0.95  # 5% less honey in Autumn

# Apply special Spring bonuses for specific flowers
if season == 'Spring' and (flower == 'Daisy' or flower == 'Mint'):
    honey = honey * 1.10  # 10% more for Daisy and Mint in Spring
"""

print(f"Total honey harvested: {honey:.2f}")




'''
Improved Approach by AI Example
For a more maintainable solution, you could use dictionaries:
'''

"""
flower = input()
flower_quantity = int(input())
season = input()

# Base honey production per flower per season
honey_production = {
    'Spring': {'Sunflower': 10, 'Daisy': 12, 'Lavender': 12, 'Mint': 10},
    'Summer': {'Sunflower': 8, 'Daisy': 8, 'Lavender': 8, 'Mint': 12},
    'Autumn': {'Sunflower': 12, 'Daisy': 6, 'Lavender': 6, 'Mint': 6}
}

# Calculate base harvest
harvest = flower_quantity * honey_production[season][flower]

# Apply seasonal bonuses
if season == 'Summer':
    harvest *= 1.10  # 10% more honey in Summer
elif season == 'Autumn':
    harvest *= 0.95  # 5% less honey in Autumn
elif season == 'Spring' and flower in ['Daisy', 'Mint']:
    harvest *= 1.10  # 10% more for Daisy and Mint in Spring

print(f"Total honey harvested: {harvest:.2f}")
"""