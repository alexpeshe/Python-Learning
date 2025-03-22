# Read required honey for winter
required_honey = float(input())
total_honey_collected = 0

# Process bees until "Winter has come"
while True:
    bee_name = input()

    # Check if winter has arrived
    if bee_name == "Winter has come":
        break

    # Track this bee's honey production
    bee_honey = 0
    was_banished = False

    # Process 6 months of production for this bee
    for month in range(6):
        monthly_honey = float(input())
        bee_honey += monthly_honey

        # Check for negative production (banishment condition)
        if monthly_honey < 0 and not was_banished:
            print(f"{bee_name} was banished for gluttony")
            was_banished = True

    # Add this bee's total production to overall total
    total_honey_collected += bee_honey

    # Check if we've collected enough honey already
    if total_honey_collected >= required_honey:
        surplus = total_honey_collected - required_honey
        print(f"Well done! Honey surplus {surplus:.2f}.")
        exit()  # End program if enough honey collected

# If we reach here, winter has come but not enough honey
shortage = required_honey - total_honey_collected
print(f"Hard Winter! Honey needed {shortage:.2f}.")


'''
Key Points:

Problem Summary
You need to track honey collection for winter

You receive the required honey amount for winter

Then you receive bee names and their monthly honey production for 6 months each

If a bee produces negative honey in a month, they're banished

The program continues until either:

"Winter has come" is received and you check if enough honey was collected

Enough honey is collected before winter comes

Key Requirements
Track total honey collected across all bees

Check if any bee has negative production in a month (banishment)

After "Winter has come" or enough honey is collected, compare with required amount

 key insights for this problem:

Use a nested loop structure - outer loop for bees, inner loop for months

Track both individual bee production and total production

Check for banishment conditions during monthly collection

Format output to 2 decimal places as required

This problem combines several concepts: input processing, nested loops, conditional logic, and early program termination based on conditions.'''