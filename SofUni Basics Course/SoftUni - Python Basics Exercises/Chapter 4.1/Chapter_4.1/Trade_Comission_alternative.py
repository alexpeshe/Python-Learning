commissions = {
    'Sofia': [(500, 0.05), (1000, 0.07), (10000, 0.08), (float('inf'), 0.12)],
    'Plovdiv': [(500, 0.055), (1000, 0.08), (10000, 0.12), (float('inf'), 0.145)],
    'Varna': [(500, 0.045), (1000, 0.075), (10000, 0.10), (float('inf'), 0.13)]
}

# Defining a dictionary called commissions, where:
# The keys are city names: 'Sofia', 'Plovdiv', and 'Varna'.
# The values are lists of tuples. Each tuple represents:
# A sales threshold (like 500, 1000, or 10000). The commission rate for that range of sales.

'''
For example:

In Sofia: If sales are <= 500, the commission rate is 5% (0.05). 
If sales are greater than 500 but <= 1000, the rate is 7% (0.07), and so on.
float('inf') represents infinity, which means sales over 10000 get the last rate.
'''

city = input()
sales = float(input())
result = 'error'

# The Input
'''
We get the city name from the user via input().
We get the sales amount, which is converted to a float, as sales can be a decimal number.
We set result = 'error' as a default value in case the city or sales input is invalid.
'''

if city in commissions and sales >= 0:

# Checking City and Sales Conditions
'''
This if condition checks two things:

Is the city valid?: city in commissions checks if the input city exists in the commissions dictionary.
Are sales non-negative?: sales >= 0 ensures that the sales are a valid, positive number.
'''
    for threshold, rate in commissions[city]:
        if sales <= threshold:
            result = sales * rate
            break

# Looping Through Commission Rates:
'''
This is  what happens in this loop:

For Loop:

The loop goes through each tuple (threshold, rate) in the list for the given city.
Example: For Sofia, it will first check (500, 0.05), then (1000, 0.07), etc.
Condition:

For each tuple, we check if the sales value is less than or equal to the threshold.
Example: If sales = 700, it will match (1000, 0.07) because 700 <= 1000.
Calculate the Commission:

When a match is found, we multiply sales by the corresponding rate and store the result in result.
Break:

After finding the correct rate, we stop the loop with break because we don’t need to check further conditions.

'''

if type(result) == str:
    print(result)
else:
    print(f"{result:.2f}")

# The Output:
'''
If result is still 'error', we print it (because either the city or sales was invalid).
If result is a valid number (float), we format it to 2 decimal places using {:.2f} and print it. This is important for commission values like "120.00", "27.50", etc.

'''