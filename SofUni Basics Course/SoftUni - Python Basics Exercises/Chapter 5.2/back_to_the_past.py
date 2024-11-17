import math  # Importing the math module, although it's not used in this code.

# Input the amount of inheritance from the user and convert it to a float.
inherited = float(input())

# Input the year until which the user plans to live and convert it to an integer.
year_until_living = int(input())

# Initialize the variable 'years' to 18, representing the starting age.
years = 18

# Loop through each year from 1800 to the year until living (inclusive).
for cy in range(1800, year_until_living + 1):  # cy stands for current_year
    # Check if the current year is even.
    if cy % 2 == 0:
        # If the year is even, subtract 12,000 from the inherited amount.
        inherited -= 12000
    else:
        # If the year is odd, subtract 12,000 plus 50 times the current age from the inherited amount.
        inherited -= (12000 + 50 * years)
    
    # Increment the age by 1 for the next year.
    years += 1

# After the loop, check if there is any inheritance left.
if inherited > 0:
    # If there is money left, print a message indicating a carefree life and the amount left.
    print('Yes! He will live a carefree life and will have "{:,.2f}" dollars left.'.format(abs(inherited)))
else:
    # If there is no money left, print a message indicating he will need more money to survive.
    print('No! He will need "{:,.2f}" dollars to survive.'.format(abs(inherited)))