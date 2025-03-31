#Fan Shop Purchase Calculator

"""
This program calculates whether a fan has enough budget to buy merchandise items from a fan shop. Let me explain the code with detailed comments:
"""

# Get input from the user
budget = int(input())  # The total budget available for shopping
n = int(input())       # The number of items the fan wants to buy
total_amount = 0       # Initialize the total cost of all items to 0

# Loop through each item to calculate the total cost
for item in range(0, n):
    input_item = input()  # Get the name of the current item
    
    # Add the price of the item to the total based on what type of item it is
    if 'hoodie' == input_item:
        total_amount += 30    # Hoodies cost 30 lv
    elif 'keychain' == input_item:
        total_amount += 4     # Keychains cost 4 lv
    elif 't-shirt' == input_item:
        total_amount += 20    # T-shirts cost 20 lv
    elif 'flags' == input_item:
        total_amount += 15    # Flags cost 15 lv
    elif 'sticker' == input_item:
        total_amount += 1     # Stickers cost 1 lv

# Calculate the difference between the total cost and the budget
diff = abs(total_amount - budget)  # Using abs() to get the absolute value of the difference

# Check if the fan has enough money and display the appropriate message
if total_amount <= budget:
    print(f"You bought {n} items and left with {diff} lv.")  # Success message with remaining money
else:
    print(f"Not enough money, you need {diff} more lv.")  # Insufficient funds message


#Concepts Learned

'''Input Processing: The program takes user input for the budget, number of items, and the name of each item.

Loop Iteration: A for loop is used to process each item purchase.

Conditional Logic: if-elif statements are used to determine the price of each item based on its name.

Accumulation Pattern: The variable total_amount is used to accumulate the cost of all items.

Absolute Value Function: The abs() function is used to calculate the absolute difference between the total cost and budget, ensuring a positive value regardless of which is larger.

String Comparison: The program compares string values to identify item types ('hoodie' == input_item).

Conditional Output: Different messages are displayed based on whether the fan has enough money.

String Formatting: F-strings are used to create readable output messages that include variable values.

Budget Management: The program implements a simple budget management system, comparing expenses against available funds.

Dictionary-like Logic: While not using an actual dictionary, the program implements a mapping between item names and their prices using conditional statements.

This program demonstrates how to track expenses against a budget, process a variable number of items, and provide appropriate feedback based on the financial outcome.'''