goods = int(input())  # number of loads

van = 0
truck = 0
train = 0
total_tons = 0

# Calculate tons for each vehicle type
for i in range(goods):
    tons = int(input())  # weight of current load
    total_tons += tons  # total weight of all loads

    # Categorize loads by weight
    if tons <= 3:
        van += tons
    elif tons <= 11:
        truck += tons
    else:
        train += tons

# Calculate total price
total_price = (van * 200) + (truck * 175) + (train * 120)

# Calculate average price per ton
avg_price = total_price / total_tons

# Calculate percentages
van_percent = (van / total_tons) * 100
truck_percent = (truck / total_tons) * 100
train_percent = (train / total_tons) * 100

# Print results
print(f"{avg_price:.2f}")
print(f"{van_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")

#Problem - solving plan

# Read total number of loads
# Initialize variables for tracking
# For each load:
#   1. Read load weight
#   2. Categorize load by weight
#   3. Add to appropriate vehicle tons
# Calculate total tons
# Calculate total price
# Calculate percentages
# Print results