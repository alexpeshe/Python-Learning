# Get input amount in decimal form (e.g., 2.50)
n = float(input())

# Convert to cents/smallest unit (e.g., 250)
n = n * 100
count = 0    # Initialize counter for number of coins/bills

if n < 0:
    print("Please enter a positive amount")
    exit()

# Continue while there's still money to convert
while n > 0:
    # Check each denomination from largest to smallest
    if n >= 200:        # 2.00 units
        n -= 200
        count += 1
    elif n >= 100:      # 1.00 units
        n -= 100
        count += 1
    elif n >= 50:       # 0.50 units
        n -= 50
        count += 1
    elif n >= 20:       # 0.20 units
        n -= 20
        count += 1
    elif n >= 10:       # 0.10 units
        n -= 10
        count += 1
    elif n >= 5:        # 0.05 units
        n -= 5
        count += 1
    elif n >= 2:        # 0.02 units
        n -= 2
        count += 1
    elif n >= 1:        # 0.01 units
        n -= 1
        count += 1

# Print total number of coins/bills needed
print(count)

'''
Key Points:

Works with denominations: 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01

Always uses largest possible denomination first

Counts total pieces needed

Converts decimal input to whole numbers for easier calculation

'''

'''
def alternative solution

def count_denominations(amount):
    # Define denominations in cents
    DENOMINATIONS = [200, 100, 50, 20, 10, 5, 2, 1]
    
    # Convert to cents and initialize
    cents = round(amount * 100)
    total_count = 0
    
    # Count each denomination
    for denom in DENOMINATIONS:
        pieces = cents // denom
        total_count += pieces
        cents %= denom
    
    return total_count

# Usage
amount = float(input())
print(count_denominations(amount))

'''

"""This alternative is:

More maintainable

Easier to modify denominations

More efficient

Less prone to errors

Easier to read and understand

The original code works but could be improved for better maintainability and efficiency"""