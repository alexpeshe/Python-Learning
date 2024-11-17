# Read the number of inputs
n = int(input())

# Counters for divisibility
divisible_by_2 = 0
divisible_by_3 = 0
divisible_by_4 = 0

# Loop through all numbers
for i in range(n):
    number = int(input())

    # Check divisibility and increment counters
    if number % 2 == 0:
        divisible_by_2 += 1
    if number % 3 == 0:
        divisible_by_3 += 1
    if number % 4 == 0:
        divisible_by_4 += 1

# Calculate percentages
p1 = (divisible_by_2 / n) * 100
p2 = (divisible_by_3 / n) * 100
p3 = (divisible_by_4 / n) * 100

# Print percentages with 2 decimal places
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")