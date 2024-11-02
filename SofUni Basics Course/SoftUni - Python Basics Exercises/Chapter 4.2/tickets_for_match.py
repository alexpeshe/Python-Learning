budget = float(input())
category = input()
people = int(input())

t_charges = 0
ticket_money = 0
money_difference = 0
result = 0

if 1 >= people <= 4:
    t_charges = budget * 0.75
elif 5 >= people <= 9:
    t_charges = budget * 0.6
elif 10 >= people <= 24:
    t_charges = budget * 0.5
elif 25 >= budget <= 49:
    t_charges = budget * 0.4
else:
    t_charges = budget * 0.25

if category == 'Normal':
    ticket_money = budget * 249.99
elif category == 'VIP':
    ticket_money = budget * 499.99

if money_difference == budget - t_charges - ticket_money:
    result = f"Yes you have {abs(money_difference):.2f)leva}"
elif money_difference < 0:
    result = "Not enough money" | f"You need {abs(money_difference):.2f) leva}" 

print(result)