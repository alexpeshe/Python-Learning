product = input()
day_of_week = input()
quantity = float(input())

result = 0
if day_of_week == 'Saturday' or day_of_week == "Sunday":
    if product == 'banana':
        result = quantity * 2.70
    elif product == 'apples':
        result == quantity * 1.25
    elif product == 'orange':
        result == quantity * 0.85
    elif product == 'grapefruit':
        result == quantity * 1.45
    elif product == 'kiwi':
        result == quantity * 2.70
    elif product == 'pineapple':
        result == quantity * 5.50
    elif product == 'grapes':
        result == quantity * 3.85
    else:
        result = 'error' 
    
#TODO finish the code

else:
    if product == 'banana':
        result = quantity * 2.50
    elif product == 'apples':
        result == quantity * 1.20
    elif product == 'orange':
        result == quantity * 0.90
    elif product == 'grapefruit':
        result == quantity * 1.60
    elif product == 'kiwi':
        result == quantity * 3.00
    elif product == 'pineapple':
        result == quantity * 5.60
    elif product == 'grapes':
        result == quantity * 4.20
    else:
        result = 'error' 
   
# TODO finish the code

print(result)


# Optimised program without code repetitiveness 

''' product = input()
day_of_week = input()
quantity = float(input())

# Define prices for each product on weekends and weekdays
prices_weekend = {
    'banana': 2.70,
    'apples': 1.25,
    'orange': 0.85,
    'grapefruit': 1.45,
    'kiwi': 2.70,
    'pineapple': 5.50,
    'grapes': 3.85
}

prices_weekday = {
    'banana': 2.50,
    'apples': 1.20,
    'orange': 0.90,
    'grapefruit': 1.60,
    'kiwi': 3.00,
    'pineapple': 5.60,
    'grapes': 4.20
}

# Determine which price list to use based on the day of the week
if day_of_week == 'Saturday' or day_of_week == "Sunday":
    prices = prices_weekend
else:
    prices = prices_weekday

# Calculate the result
result = prices.get(product, 'error') * quantity

print(result)
'''