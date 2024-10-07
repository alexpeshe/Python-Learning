w = float(input())
h = float(input())

w_to_cm = w * 100
h_to_cm = h * 100

rows = int(w_to_cm / 120) # the alternative iis //

h_to_cm -= 100 # equal to h_to_cm = h_to_cm - 100
row_buros = h_to_cm//70

all_buros = rows*row_buros - 3
print(all_buros)

