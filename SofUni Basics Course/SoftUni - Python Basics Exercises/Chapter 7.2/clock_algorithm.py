# Input Section
symbol_1 = int(input())    # Takes first input and converts it to integer
symbol_2 = int(input())    # Takes second input and converts it to integer
symbol_3 = input()         # Takes third input as string
symbol_4 = input()         # Takes fourth input as string
symbol_5 = int(input())    # Takes fifth input and converts it to integer

# Commented out inputs (currently not in use)
# symbol_6 = int(input())  # Disabled sixth input
# symbol_7 = int(input())  # Disabled seventh input
# symbol_8 = int(input())  # Disabled eighth input

# Attempting to combine all symbols (Note: This will cause an error)
symbol_range = symbol_1+symbol_2+symbol_3+symbol_4+symbol_5  # This line will raise a TypeError because you can't add integers and strings

# Nested loops for time
for i in range(0, 24):                # Outer loop for hours (0-23)
    print('hour' +str(i))             # Prints current hour
    
    for minutes in range(0, 60):      # Middle loop for minutes (0-59)
        print('minutes' +str(minutes)) # Prints current minute
        
        for seconds in range(0, 60):   # Inner loop for seconds (0-59)
            print('minutes' +str(seconds)) # Prints current second (Note: Label says 'minutes' but should be 'seconds')


'''
Issues and Notes:

The symbol_range calculation will raise an error because it tries to add integers (symbol_1, symbol_2, symbol_5) with strings (symbol_3, symbol_4)

The time-printing loops will output:

All 24 hours (0-23)

For each hour, all 60 minutes (0-59)

For each minute, all 60 seconds (0-59)

There's a labeling error in the seconds loop where it prints "minutes" instead of "seconds"

This code will generate 24 * 60 * 60 = 86,400 lines of output

Suggested Fix for symbol_range (if needed):
'''

# Alternative: symbol_range = str(symbol_1) + str(symbol_2) + symbol_3 + symbol_4 + str(symbol_5)  # Convert all to strings for concatenation
