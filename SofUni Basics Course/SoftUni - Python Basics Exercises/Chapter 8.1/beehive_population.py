# My solution:

initial_population = int(input())
years = int(input())

born_bees = 0
dead_bees = 0
migrated_bees = 0

population = initial_population

for year in range(1, years+1):
    # Calculate births at the beginning of every year
    new_births = population // 10 * 2
    born_bees += new_births
    population += new_births
    
    # Check if it's a 5th year (when migration happens)
    if year % 5 == 0:
        # It's a 5th year - both migration and deaths occur
        migrants = population // 50 * 5
        migrated_bees += migrants
        population -= migrants
        
    # Deaths occur at the end of every year
    deaths = population // 20 * 2
    dead_bees += deaths
    population -= deaths

print(f'Beehive population: {population}')

'''print(f'Total bees born: {born_bees}')
print(f'Total bees died: {dead_bees}')
print(f'Total bees migrated: {migrated_bees}')'''


"""
SoftUni's Solution

initial_population = int(input())
years = int(input())

population = initial_population

for i in range(1, years+1):
    # This is the part where births happen at the beginning of every year
    population += population // 10 * 2

    # Check if it's a 5th year (when migration happens)
    if i % 5 != 0:
         # Not a 5th year - only deaths occur
        population -= population // 20 * 2
    elif i % 5 == 0:
        # It's a 5th year - both migration and deaths occur
        population -= (population // 50 * 5)
        population -= (population // 20 * 2)

print(f'Beehive population: {population}')
"""

'''
Key Points:

Sequential Logic and Simulation: The ability to model a system that changes over time according to specific rules. You need to understand how to apply multiple operations in the correct sequence.

Integer Division: The problem requires using integer division (//) to calculate whole numbers of bees for births, deaths, and migrations.

Conditional Logic: Understanding how to apply different rules based on conditions (specifically handling every 5th year differently).

Loop Implementation: Using a loop to simulate multiple years and correctly tracking the changing population.

Order of Operations: Understanding that the sequence matters - births happen first, then migration (if applicable), then deaths.

Modular Arithmetic: Using the modulo operator (%) to identify every 5th year.

Variable Manipulation: Properly updating a running total based on calculated changes.
'''

'''
Knowing what range to use:

Knowing whether to use +1, +2, or another value in your range depends on understanding the relationship between your starting point, ending point, and what you're trying to count. Here's a simple framework to help you decide:

Basic Rule for range(start, end)
The range will include start but exclude end

It generates numbers: start, start+1, start+2, ..., end-1

How to Determine the Correct End Value
Identify what you're counting:

Are you counting from 0 or from 1?

How many items total do you need to count?

Apply this formula:
end = start + number_of_items

For common scenarios:

If starting from 0 and need n items: range(0, n)

If starting from 1 and need n items: range(1, n+1)

If starting from any number x and need n items: range(x, x+n)

Examples:
Count years 1 through 6:

Start: 1

Items needed: 6

Range: range(1, 1+6) = range(1, 7)

Count 10 items starting from 0:

Start: 0

Items needed: 10

Range: range(0, 0+10) = range(0, 10)

Count days 5 through 12:

Start: 5

Items needed: 8 (days 5,6,7,8,9,10,11,12)

Range: range(5, 5+8) = range(5, 13)

The key is to remember that you need to add the number of items you want to the starting point to get the correct ending value for your range.

'''