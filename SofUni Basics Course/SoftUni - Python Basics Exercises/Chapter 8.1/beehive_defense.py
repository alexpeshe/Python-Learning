# My solution:
bees = int(input())
bear_health = int(input())
bear_attack = int(input())

# Battle continues until bear dies or bees fall below 100
while bear_health > 0 and bees >= 100:
    # Bear attacks first
    bees -= bear_attack
    if bees < 0:
        bees = 0  # Bees can't be negative

    # If bees are still enough, they counter-attack
    if bees >= 100:
        bear_health -= bees * 5  # Each bee does 5 damage

# Determine the winner and print result
if bear_health <= 0:
    print(f"Beehive won! Bees left {bees}.")
else:
    print(f"The bear stole the honey! Bees left {bees}.")


# SoftUni's

"""
bees_qty = int(input())
bear_hp = int(input())
bear_power = int(input())

bees_left = bees_qty

while bees_left >= 100:
    bees_left = bees_left-bear_power
    bear_hp = bear_hp-bees_left * 5
    if bear_hp <= 0:
        print(f'Beehive won! Bees left {bees_left}.')
        break

if bees_left <= 0:
    bees_left = 0
    print(f'The bear stole the honey! Bees left {bees_left}.')
elif bees_left < 100:
    print(f'The bear stole the honey! Bees left {bees_left}.')
"""