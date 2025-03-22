# My solution:

# Import the math module to use the floor function
import math

# Get input values from the user
bees = int(input())      # Number of bees (integer between 1-1000)
flowers = int(input())   # Number of flowers (integer between 1-10000)

# Define the capacity of one honeycomb in grams
honeycomb = 100 

# Calculate the total honey produced
# Each bee produces 0.21 grams of honey from each flower
honey = bees * flowers * 0.21

# Calculate how many complete honeycombs can be filled
# Using floor division to get only complete honeycombs
honeymade = math.floor(honey / honeycomb)

# Calculate how much honey is left after filling complete honeycombs
honey_left = honey - (honeymade * 100)

# Print the results according to the required format
print(f"{honeymade} honeycombs filled.")
print(f"{honey_left:.2f} grams of honey left")

