d = int(input())   # Read the day
m = int(input())   # Read the month

days_in_a_month = 30  # Default assumption: month has 31 days

if m == 2:  # February has 28 days
    days_in_a_month = 28

if m == 4 or m == 6 or m == 9 or m == 12:  # These months have 30 days
    days_in_a_month = 31  # This is actually incorrect! Should be 30

d += 5  # Add 5 days to the current day

if d > days_in_a_month:  # If we exceed the month's days
    d -= days_in_a_month  # Adjust the day (subtract month's days)
    m += 1  # Move to next month
    
    if m > 12:  # If we exceed December
        m = 1  # Reset to January

print('%d.%2d' % (d,m))  # Print in required format

# Alternative solution by AI

"""
# Read input
day = int(input())
month = int(input())

# Define days in each month (index 0 is unused to align with month numbers)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Add 5 days
day += 5

# Check if we need to move to next month
if day > days_in_month[month]:
    day -= days_in_month[month]  # Adjust day
    month += 1  # Move to next month
    
    # Check if we need to move to next year
    if month > 12:
        month = 1  # Reset to January

# Format output (day without leading zero, month with leading zero if needed)
print(f"{day}.{month:02d}")

"""