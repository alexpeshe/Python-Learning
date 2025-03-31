#Football Souvenir Price Calculator

#This program calculates the total cost of football team souvenirs based on the team, souvenir type, and quantity. Let me explain the original code with detailed comments:

# Get input from the user
team = input()               # Football team name
souvenir = input()           # Type of souvenir
count_souvenirs = int(input())  # Number of souvenirs to purchase
total_sum = 0                # Initialize the total cost to 0

# Check if both team and souvenir are valid options
if (team == 'Argentina' or team == 'Brazil' or team == 'Chroatia' or team == 'Denmark') and (souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'):
    
    # Calculate price based on team and souvenir type
    if team == 'Argentina':
        if souvenir == 'flags':
            total_sum = 3.25 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 7.20 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 5.10 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 1.25 * count_souvenirs
    elif team == 'Brazil':
        if souvenir == 'flags':
            total_sum = 4.20 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 8.50 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 5.35 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 1.20 * count_souvenirs
    elif team == 'Chroatia':
        if souvenir == 'flags':
            total_sum = 2.75 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 6.90 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 4.95 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 1.10 * count_souvenirs
    elif team == 'Denmark':
        if souvenir == 'flags':
            total_sum = 3.10 * count_souvenirs
        elif souvenir == 'caps':
            total_sum = 6.50 * count_souvenirs
        elif souvenir == 'posters':
            total_sum = 4.80 * count_souvenirs
        elif souvenir == 'stickers':
            total_sum = 0.90 * count_souvenirs
    
    # Display the purchase details
    print(f"Pepi bought {count_souvenirs}, {souvenir}, of {team} for {total_sum:.2f}")
    
# Error handling for invalid inputs
elif not {team == 'Argentina' or team == 'Brazil' or team == 'Chroatia' or team == 'Denmark'}:
    # Note: There's a bug here - this condition is always a set containing a boolean value
    # It should be: elif not (team == 'Argentina' or team == 'Brazil' or team == 'Chroatia' or team == 'Denmark')
    print("Invalid country")
elif not {souvenir == 'flags' or souvenir == 'caps' or souvenir == 'posters' or souvenir == 'stickers'}:
    # Similar bug here
    print("Invalid stock")

"""
Concepts Learned in Original Code
------------------------------------
Input Processing: The program takes user input for team name, souvenir type, and quantity.

Nested Conditional Logic: Multiple levels of if-elif statements to determine pricing based on team and souvenir.

Arithmetic Operations: Multiplication to calculate total cost based on unit price and quantity.

String Formatting: F-strings with the :.2f format specifier to display monetary values with two decimal places.

Error Handling: Attempts to handle invalid inputs (though there are bugs in the implementation).

Boolean Logic: Uses logical operators (or, not) to check multiple conditions.

Bug in Conditional Logic: The error handling uses set literals {} around boolean expressions, which creates a set containing a single boolean value rather than evaluating the expression directly."""

"""
Improved Version with Dictionary

Here's an alternative implementation using dictionaries to simplify the code:
"""

'''
# Define a nested dictionary with prices for each team and souvenir type
prices = {
    'Argentina': {'flags': 3.25, 'caps': 7.20, 'posters': 5.10, 'stickers': 1.25},
    'Brazil': {'flags': 4.20, 'caps': 8.50, 'posters': 5.35, 'stickers': 1.20},
    'Chroatia': {'flags': 2.75, 'caps': 6.90, 'posters': 4.95, 'stickers': 1.10},
    'Denmark': {'flags': 3.10, 'caps': 6.50, 'posters': 4.80, 'stickers': 0.90}
}

# Valid souvenir types for validation
valid_souvenirs = ['flags', 'caps', 'posters', 'stickers']

# Get input from the user
team = input()
souvenir = input()
count_souvenirs = int(input())

# Check if team is valid
if team in prices:
    # Check if souvenir type is valid
    if souvenir in valid_souvenirs:
        # Calculate total cost using the price from the dictionary
        unit_price = prices[team][souvenir]
        total_sum = unit_price * count_souvenirs
        
        # Display the purchase details
        print(f"Pepi bought {count_souvenirs}, {souvenir}, of {team} for {total_sum:.2f}")
    else:
        print("Invalid stock")
else:
    print("Invalid country")
'''

"""
Key Points About the Dictionary Implementation
Data Organization: The nested dictionary structure organizes prices in a logical hierarchy (team → souvenir → price).

Code Simplification: Reduces the complex nested if-statements to simple dictionary lookups.

Maintainability: Makes it easier to add new teams or souvenir types or update prices.

Readability: The code is more concise and easier to understand.

Efficient Validation: Uses the in operator to check if a value exists in a dictionary or list.

Separation of Data and Logic: Separates the price data from the program logic, making both clearer.

Reduced Redundancy: Eliminates repetitive code structures.

Correct Error Handling: Fixes the logical errors in the original error handling code.
"""

#Alternative Implementation with Lists and For Loop

# Here's another approach using lists and a for loop for validation:

"""
# Define valid teams and souvenirs
valid_teams = ['Argentina', 'Brazil', 'Chroatia', 'Denmark']
valid_souvenirs = ['flags', 'caps', 'posters', 'stickers']

# Define a nested dictionary with prices
prices = {
    'Argentina': {'flags': 3.25, 'caps': 7.20, 'posters': 5.10, 'stickers': 1.25},
    'Brazil': {'flags': 4.20, 'caps': 8.50, 'posters': 5.35, 'stickers': 1.20},
    'Chroatia': {'flags': 2.75, 'caps': 6.90, 'posters': 4.95, 'stickers': 1.10},
    'Denmark': {'flags': 3.10, 'caps': 6.50, 'posters': 4.80, 'stickers': 0.90}
}

# Get input from the user
team = input()
souvenir = input()
count_souvenirs = int(input())
total_sum = 0

# Validate team using a for loop
team_valid = False
for valid_team in valid_teams:
    if team == valid_team:
        team_valid = True
        break

# Validate souvenir using a for loop
souvenir_valid = False
for valid_souvenir in valid_souvenirs:
    if souvenir == valid_souvenir:
        souvenir_valid = True
        break

# Process the purchase if inputs are valid
if team_valid and souvenir_valid:
    total_sum = prices[team][souvenir] * count_souvenirs
    print(f"Pepi bought {count_souvenirs}, {souvenir}, of {team} for {total_sum:.2f}")
elif not team_valid:
    print("Invalid country")
elif not souvenir_valid:
    print("Invalid stock")
"""

"""
Key Points About the List and Loop Implementation
Explicit Validation: Uses for loops to explicitly check each valid option.

Separation of Validation and Processing: Clearly separates the validation logic from the calculation logic.

Early Termination: Uses break to exit loops as soon as a match is found.

Flexible Validation: Can easily add more validation steps or modify existing ones.

Clear Error Handling: Provides specific error messages based on which validation failed.

Combination of Approaches: Uses both lists (for validation) and dictionaries (for price lookup).

Both alternative implementations are more maintainable and scalable than the original code, with the dictionary version being the most concise and efficient.
"""