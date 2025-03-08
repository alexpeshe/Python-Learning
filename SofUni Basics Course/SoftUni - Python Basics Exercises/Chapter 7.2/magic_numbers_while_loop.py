# Get user input for target number
n = int(input())    # Convert string input to integer
result = ''         # Initialize empty string to store results

# Initialize counters for each digit
a = 1
while a < 10:
    b = 1
    while b < 10:
        c = 1
        while c < 10:
            d = 1
            while d < 10:
                e = 1
                while e < 10:
                    f = 1
                    while f < 10:
                        # Check if multiplication of digits equals target number
                        if a*b*c*d**e*f == n:
                            # If condition met, concatenate digits to result string
                            result += ('' + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + ' ')
                        f += 1
                    e += 1
                d += 1
            c += 1
        b += 1
    a += 1

# Print all found combinations
print(result)

'''
Key differences and notes with for loops version:

Structure Differences:

Each loop counter needs to be initialized before the while loop

Manual increment of counters needed (e.g., a += 1)

Condition checking is done at the start of each loop

Enhanced Version with More Control:'''

'''
Purpose of Counter Initialization
Starting Point:

Each variable (a, b, c, d, e, f) starts at 1 because:

We want to check digits 1-9

Zero is excluded as it would make multiplication zero

Loop Control:

These variables control how many times each loop iterates

They're incremented inside the loop (a += 1, b += 1, etc.)

The loop continues until each counter reaches 9

a = 1    # Initialize first digit counter
while a < 10:    # Loop will run while a is less than 10 (1-9)
    b = 1    # Initialize second digit counter
    while b < 10:
        c = 1    # Initialize third digit counter
        while c < 10:
            # ... and so on
'''

# Enhanced Version with More Control:

'''
def find_magic_numbers_while():
    n = int(input())
    result = ''
    
    a = 1
    while a < 10:
        b = 1
        while b < 10:
            c = 1
            while c < 10:
                d = 1
                while d < 10:
                    e = 1
                    while e < 10:
                        f = 1
                        while f < 10:
                            try:
                                if a*b*c*d**e*f == n:
                                    result += f"{a}{b}{c}{d}{e}{f} "
                            except OverflowError:
                                pass  # Handle large number calculations
                            f += 1
                        e += 1
                    d += 1
                c += 1
            b += 1
        a += 1
    
    return result.strip()

# With error handling and user input validation
try:
    result = find_magic_numbers_while()
    if result:
        print("Found combinations:", result)
    else:
        print("No combinations found")
except ValueError:
    print("Please enter a valid number")
'''

'''
Advantages of While Loop Version:

More flexible control over iteration

Easier to add break conditions

Can modify counters within the loop

Disadvantages of While Loop Version:

More verbose

More prone to infinite loops if not careful

Requires manual counter management
'''

# Alternative def Version with Break Conditions:

'''

def find_magic_numbers_while_with_breaks():
    n = int(input())
    result = ''
    
    a = 1
    while a < 10:
        # Early exit if first number is too large
        if a > n:
            break
            
        b = 1
        while b < 10:
            c = 1
            while c < 10:
                # Check if partial product is already too large
                if a*b*c > n:
                    break
                    
                d = 1
                while d < 10:
                    e = 1
                    while e < 10:
                        f = 1
                        while f < 10:
                            try:
                                if a*b*c*d**e*f == n:
                                    result += f"{a}{b}{c}{d}{e}{f} "
                            except OverflowError:
                                break  # Skip if numbers get too large
                            f += 1
                        e += 1
                    d += 1
                c += 1
            b += 1
        a += 1
    
    return result.strip()

    '''


