# Get user inputs and convert to appropriate format
month = input().lower()           # Convert month to lowercase for comparison
hours = int(input())             # Number of hours
people = int(input())            # Number of people
day_or_night = input().lower()   # Time of day (day/night)

result = 0    # Initialize price per person per hour

# Spring pricing (March, April, May)
if month == "march" or month == "april" or month == "may":
    if day_or_night == 'day':
        result = 10.5    # Day rate
    else:
        result = 8.4     # Night rate

# Summer pricing (June, July, August)
elif month == "june" or month == "july" or month == "august":
    if day_or_night == 'night':
        result = 12.6    # Night rate
    else:
        result = 10.2    # Day rate

# Apply group discount (10% off for 4 or more people)
if people >= 4:
    result = result - result*0.10
    #alternative 
    # result = result*0.9

# Apply duration discount (50% off for 5 or more hours)
if hours >= 5:
    result = result - result*0.50

# Calculate total cost
sum = result*people

# Print results formatted to 2 decimal places
print(f"Price per person for one hr: {result:.2f}")
print(f"Total cost of the visit: {sum:.2f}")

"""
Key Points:
----------------------------------------------------------
Separate if statements allow both conditions to be checked

Both discounts can apply if conditions are met

Discounts stack (multiply) with each other

The order matters for the final calculation

Also:

The difference is:

With elif: Only ONE season block will execute (either Spring OR Summer)

With if: Both blocks would be checked independently, and the second if could override the first one's result

We use elif because:

A month can't be in both Spring and Summer

We want only one season's pricing to apply

The second condition should only be checked if the first one is False

Think of it like a decision tree:

Is it Spring? No → Check if it's Summer

Is it Spring? Yes → Don't even check Summer"""

"""
Key Components:
Seasonal Pricing

Spring (March-May)

Day: 10.50

Night: 8.40

Summer (June-August)

Day: 10.20

Night: 12.60

Discounts

Group Discount: 10% off for 4+ people

Duration Discount: 50% off for 5+ hours

Input Processing

Converts month and time to lowercase

Converts hours and people to integers
"""