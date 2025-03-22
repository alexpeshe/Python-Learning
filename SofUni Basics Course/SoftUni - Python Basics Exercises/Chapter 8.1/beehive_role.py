# My solution:

intelligence = int(input())
strength = int(input())
gender = input().lower()

# Check roles in order of priority
if intelligence >= 80 and strength >= 80 and gender == 'female':
    print('Queen Bee')
elif intelligence >= 80:
    print('Repairing Bee')
elif intelligence >= 60:
    print('Cleaning Bee')
elif strength >= 80 and gender == 'male':
    print('Drone Bee')
elif strength >= 60:
    print('Guard Bee')
else:
    print('Worker Bee')

# Notes

"""
Check Roles in the Correct Order:

First check Queen Bee (highest priority)

Then check other intelligence-based roles (Repairing Bee, Cleaning Bee)

Then check strength-based roles (Drone Bee, Guard Bee)

Finally, default to Worker Bee if no other role fits


Verify Role Requirements:
Double-check each role's requirements against the problem statement:

Queen Bee: Intelligence ≥80, Strength ≥80, Female

Repairing Bee: Intelligence ≥80, Any strength, Any gender

Cleaning Bee: Intelligence ≥60, Any strength, Any gender

Drone Bee: Any intelligence, Strength ≥80, Male

Guard Bee: Any intelligence, Strength ≥60, Any gender

Worker Bee: Any intelligence, Any strength, Any gender


Simplify Conditions:

Remove redundant conditions to make your code cleaner:

gender == 'female' or gender == 'male' is unnecessary

strength >= 0 is unnecessary since all values are 1-100

intelligence >= 0 is also unnecessary
"""

