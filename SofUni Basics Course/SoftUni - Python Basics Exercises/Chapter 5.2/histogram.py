
# Define total number of inputs to process
numbers = 3

# Initialize counters for each range category to 0
p1 = 0  # Counter for numbers < 200
p2 = 0  # Counter for numbers between 200-399
p3 = 0  # Counter for numbers between 400-598
p4 = 0  # Counter for numbers between 599-799
p5 = 0  # Counter for numbers >= 800

# Loop through the specified number of inputs
for number in range(0, numbers):
    # Get input from user and convert to integer
    cur_number = int(input())
    
    # Check which range the number falls into and increment appropriate counter
    if cur_number < 200:
        p1 += 1
    elif cur_number >= 200 and cur_number < 400:
        p2 += 1
    elif cur_number >= 400 and cur_number < 599:
        p3 += 1
    elif cur_number >= 599 and cur_number < 800:
        p4 += 1 
    else:  # Numbers >= 800
        p5 += 1

# Calculate and print percentages for each range
# Formula: (counter/total numbers) * 100, formatted to 2 decimal places
print(f"{p1/numbers*100:.2f}%")  # Percentage of numbers < 200
print(f"{p2/numbers*100:.2f}%")  # Percentage of numbers 200-399
print(f"{p3/numbers*100:.2f}%")  # Percentage of numbers 400-598
print(f"{p4/numbers*100:.2f}%")  # Percentage of numbers 599-799
print(f"{p5/numbers*100:.2f}%")  # Percentage of numbers >= 800










'''
numbers = 3

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(0, numbers):
    cur_number = int(input())
    if cur_number <200:
        p1 += 1
    elif cur_number >=200 and cur_number <400:
        p2 += 1
    elif cur_number >= 400 and cur_number <599:
        p3 += 1
    elif cur_number >= 599 and cur_number <800:
        p4 += 1 
    else:
        p5 += 1

print(f"{p1/numbers*100:.2f}%")
print(f"{p2/numbers*100:.2f}%")
print(f"{p3/numbers*100:.2f}%")
print(f"{p4/numbers*100:.2f}%")
print(f"{p5/numbers*100:.2f}%")
'''