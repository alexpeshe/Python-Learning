'''
Stadium Income and Charity Calculation
This program calculates the total income from ticket sales at a stadium and determines the amount that will be donated to charity. Let me explain the code step by step with comments:
'''

# Get input from the user
sector = int(input())  # Number of sectors in the stadium (not used in calculations)
capacity = int(input())  # Total capacity of the stadium (number of seats)
ticket_price = float(input())  # Price per ticket in BGN (Bulgarian Lev)

# Calculate the total income from all ticket sales
all_sum = capacity * ticket_price

# Calculate the profit for a single sector
# The stadium is divided into 4 equal sectors
single_sector_profit = all_sum / 4

# Calculate the charity amount
# Formula: (total income - (profit from one sector * 0.75)) / 8
# This means 75% of one sector's income is kept, and the rest is divided by 8 for charity
charity = (all_sum - (single_sector_profit * 0.75)) / 8

# Display the results, formatted to 2 decimal places
print(f"Total income - {all_sum:.2f} BGN")
print(f"Money for charity - {charity:.2f} BGN")

# Concepts Learned

'''
Input Processing: The program takes user input and converts it to appropriate data types (integers and floats).

Basic Arithmetic Operations: The code demonstrates multiplication, division, and subtraction to calculate the total income, sector profit, and charity amount.

Financial Calculations: The program models a real-world financial scenario with specific business rules about how income is distributed.

String Formatting: The f-string syntax is used with the :.2f format specifier to display monetary values with exactly two decimal places.

Variable Assignment: Values are stored in appropriately named variables that make the code readable and maintainable.

Business Logic Implementation: The program implements specific business rules (dividing the stadium into 4 sectors, keeping 75% of one sector's profit, dividing the remainder by 8 for charity).'''