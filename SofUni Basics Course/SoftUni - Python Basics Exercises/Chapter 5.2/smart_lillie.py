# Get input from user
age = int(input())  # Get age as integer
wm_price = float(input())  # Get washing machine price as float
toy_price = int(input())  # Get toy price as integer

# Initialize variables
toy_count = 0  # Counter for number of toys received
sum = 0  # Total money saved
money = 10  # Initial money amount (increases by 10 each even year)
brother_money = 0  # Money taken by brother (1 dollar per even birthday)

# Loop through each year up to the age
for year in range(1, age+1):
    # Check if year is even
    if year % 2 == 0:
        sum += money  # Add current money amount to total
        money = money + 10  # Increase money for next even year
        brother_money += 1  # Brother takes 1 dollar
    # If year is odd
    else:
        toy_count += 1  # Receive a toy

# Calculate final sum
# Add money from selling toys and subtract brother's taken money
sum = sum + (toy_count * toy_price) - brother_money

# Calculate difference between saved money and washing machine price
diff = abs(sum - wm_price)

# Check if enough money was saved and print result
if sum >= wm_price:
    print('Yes! {0:.2f}'.format(diff))  # Format output to 2 decimal places
else:
    print('No! {0:.2f}'.format(diff))  # Format output to 2 decimal places

''' 
original code
if sum>= wm_price:
    diff = sum - wm_price
    print('Yes! {0:.2f}'.format((diff)))
else:
    diff = wm_price - sum
    print('No! {0:.2f}'.format(diff)) # use format() to
    '''

'''
Optimised 
 
for year in range(1, age+1):
    if year %2==0:
        money = money+10
        sum += money
        brother_money+=1
        '''

'''
for i in range etc:
    the i stands for index'''