price_veggie_kg = float(input())
price_fruit_kg = float(input())

wight_veggie_kg = float(input())
wight_fruit_kg = float(input())

veggie = price_veggie_kg*wight_veggie_kg
fruit = price_fruit_kg*wight_fruit_kg
sum = veggie+fruit

sum_euro = sum / 1.96

print(sum_euro)
