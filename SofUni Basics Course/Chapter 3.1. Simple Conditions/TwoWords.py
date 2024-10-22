first = input()
second = input()

first = first.lower()
second = second.lower()

# алтернативен метод би бил използванерто на .upper() функцията
''' first = first.upper()
second = second.upper()'''

# друг алтернативен метод би бил използванерто на вложена функцията
'''
if first.lower() = second.lower()
if first.upper() = second.upper()
'''

if first == second:
    print("yes")
else:
    print("no")
