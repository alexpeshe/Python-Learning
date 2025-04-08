import math

money_saved = float(input())
floor_width = float(input())
floor_length = float(input())
side_triangle = float(input())
h_triangle = float(input())
tile_price = float(input())
handyman_price = float(input())

# Calculate floor area
floor_area = floor_width * floor_length

# Calculate triangle tile area (triangle area = (base * height) / 2)
tile_area = (side_triangle * h_triangle) / 2

# Calculate tiles needed (rounded up) plus 5 spare tiles
tiles_needed = math.ceil(floor_area / tile_area) + 5

# Calculate total cost
total_sum = (tiles_needed * tile_price) + handyman_price

# Check if savings are sufficient
if money_saved >= total_sum:
    money_left = money_saved - total_sum
    print(f"{money_left:.2f} lv left.")

else:
    money_needed = total_sum - money_saved
    print(f"You'll need {money_needed:.2f} lv more.")

'''
alternative extra
elif money_saved == total_sum:
    # Exactly enough money
    # '''