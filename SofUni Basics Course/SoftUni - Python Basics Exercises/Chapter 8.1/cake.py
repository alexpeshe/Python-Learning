# Get initial cake dimensions
width = int(input())    # Width of the cake
length = int(input())   # Length of the cake

# Calculate total cake pieces
area = width*length     # Total number of cake pieces

# Get first input for pieces taken
data = input()

# Continue loop until "STOP" is entered
while not data == "STOP":
    # Subtract pieces taken from total
    area -= int(data)   # Remove taken pieces from remaining area
    
    # Check if we've run out of cake
    if area <= 0:
        # If no cake left or we need more pieces than we have
        print(f"No more cakes left! You need {abs(area)} pieces more.")
        break   # Exit the loop if we run out of cake
    
    # Get next input
    data = input()

# If there's cake left after stopping
if area > 0:
    print(f"{area} pieces left.")

"""
Program Flow:
----------------------
Gets cake dimensions

Calculates total pieces

Repeatedly asks for pieces taken until:

User enters "STOP" OR

Runs out of cake

Shows remaining pieces or how many more were needed
--------------------------------------------------------
--------------------------------------------------------
Key Points:
------------------------------------
Uses while loop for continuous input

Has two exit conditions (STOP or no cake left)

Handles negative remaining pieces using abs()

Different output messages based on remaining cake
"""

