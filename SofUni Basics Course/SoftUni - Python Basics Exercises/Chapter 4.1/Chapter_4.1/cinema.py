# cinema.py

type = input().lower()
rows = int(input())
columns = int(input())


full = rows * columns
income = 0

if type == "premiere":
    income = full * 12.00

elif type == "normal":
    income = full * 7.50

elif type == "discount":
    income == full * 5.00

else:
    print('error')

print("{:.2f}".format(income))

