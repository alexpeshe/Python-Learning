
# Read input values
budget = float(input())
season = input()

# Initialize variables
result = 0
destination = ''
holiday_info = '' 

# Determine destination and spending based on budget and season
if budget <= 100:
    destination = 'Bulgaria'

    if season == 'summer':
        result = budget * 0.3
        holiday_info = f"Camp - {result: .2f}"

    elif season == 'winter':
        result = budget * 0.7
        holiday_info = f"Hotel - {result: .2f}"
    

elif 100 < budget <= 1000:
    destination =  "Balkans"

    if season == 'summer':
        result = budget * 0.4
        holiday_info = f"Camp  - {result: .2f}"

    elif season == 'budget':
        result = budget * 0.8
        holiday_info = f"Hotel - {result: .2f}"

else:
    destination = 'Europe'
    result = budget * 0.9 # Always spend 90% of the budget in Europe
    holiday_info = f" Hotel  {result:.2f}"

# Print output formatted according to requirements
print(f"Somewhere in {destination}")
print(holiday_info)
