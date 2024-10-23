import math

vinyardarea = int(input())  # vineyard size in square meters
grapespsqm = float(input())  # grapes per square meter
neededlitres = int(input())  # liters of wine needed
workers = int(input())  # number of workers

# Calculate total grapes and grapes for wine production
totalgrapes = vinyardarea * grapespsqm  # total grapes harvested
grapesforwine = totalgrapes * 0.4  # 40% of grapes go for wine production

# Calculate total wine in liters
totalwine = grapesforwine / 2.5  # 1 liter requires 2.5 kg of grapes

# harvestpvine = neededlitres * grapespsqm * 0.4
# vine = harvestpvine / 2.5

# Compare total wine to the needed quantity
if totalwine >= neededlitres:
    # If there's enough wine or more
    totalwine = math.floor(totalwine)  # Round down the total wine produced
    extra_wine = totalwine - neededlitres  # Calculate extra wine
    wine_per_worker = extra_wine / workers  # Divide the extra wine among workers

    # Print the result with rounding up where needed
    print(f"Good harvest this year! Total wine: {totalwine} liters.")
    print(f"{math.ceil(extra_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    # If there's not enough wine
    insufficient_wine = neededlitres - totalwine  # Calculate the deficit
    print(f"It will be a tough winter! More {math.floor(insufficient_wine)} liters wine needed.")

