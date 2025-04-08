chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input().lower()
is_holiday = input().lower()

total_flowers = chrysanthemums + roses + tulips
total_sum = 0

# Set prices based on season
if season in ['spring', 'summer']:
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
else:  # autumn or winter
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

# Calculate initial sum
total_sum = (chrysanthemums * chrysanthemum_price) + (roses * rose_price) + (tulips * tulip_price)

# Apply holiday increase if applicable
if is_holiday == 'y':
    total_sum *= 1.15

# Apply discounts
if season == 'spring' and tulips > 7:
    total_sum *= 0.95
if season == 'winter' and roses >= 10:
    total_sum *= 0.90
if total_flowers > 20:
    total_sum *= 0.80

# Add arrangement fee
total_sum += 2

print(f"{total_sum:.2f}")
