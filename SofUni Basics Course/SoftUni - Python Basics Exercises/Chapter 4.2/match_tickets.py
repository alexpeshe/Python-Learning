# Get user input for budget, ticket category and number of people
budget = float(input())
category = input()
people = int(input())

# Initialize variables
transport_charges = 0
ticket_money = 0

# Calculate transport charges based on number of people
if people <= 4:  # 1-4 people
    transport_charges = budget * 0.75
elif 5 <= people <= 9:  # 5-9 people
    transport_charges = budget * 0.60
elif 10 <= people <= 24:  # 10-24 people
    transport_charges = budget * 0.50
elif 25 <= people <= 49:  # 25-49 people
    transport_charges = budget * 0.40
else:  # 50 or more people
    transport_charges = budget * 0.25

# Calculate ticket costs based on category
if category == 'Normal':
    ticket_money = people * 249.99  # Cost per person for Normal tickets
elif category == 'VIP':
    ticket_money = people * 499.99  # Cost per person for VIP tickets

# Calculate total expenses and remaining money
total_expenses = transport_charges + ticket_money
money_difference = budget - total_expenses

# Determine if budget is sufficient and format output
if money_difference >= 0:
    result = f"Yes! You have {money_difference:.2f} leva left."
else:
    result = f"Not enough money! You need {abs(money_difference):.2f} leva."

# Print final result
print(result)# Get user input for budget, ticket category and number of people
budget = float(input())
category = input()
people = int(input())

# Initialize variables
transport_charges = 0
ticket_money = 0

# Calculate transport charges based on number of people
if people <= 4:  # 1-4 people
    transport_charges = budget * 0.75
elif 5 <= people <= 9:  # 5-9 people
    transport_charges = budget * 0.60
elif 10 <= people <= 24:  # 10-24 people
    transport_charges = budget * 0.50
elif 25 <= people <= 49:  # 25-49 people
    transport_charges = budget * 0.40
else:  # 50 or more people
    transport_charges = budget * 0.25

# Calculate ticket costs based on category
if category == 'Normal':
    ticket_money = people * 249.99  # Cost per person for Normal tickets
elif category == 'VIP':
    ticket_money = people * 499.99  # Cost per person for VIP tickets

# Calculate total expenses and remaining money
total_expenses = transport_charges + ticket_money
money_difference = budget - total_expenses

# Determine if budget is sufficient and format output
if money_difference >= 0:
    result = f"Yes! You have {money_difference:.2f} leva left."
else:
    result = f"Not enough money! You need {abs(money_difference):.2f} leva."

# Print final result
print(result)