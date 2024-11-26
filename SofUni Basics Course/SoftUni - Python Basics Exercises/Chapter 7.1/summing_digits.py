num = input()

# easy solution

sum = 0

for i in num:
    sum = sum + int(i)

print(num)

# intened solution

'''
n = input()


sum = 0

while True:
    sum = sum + (n%10)
    n = n//10
    if not n > 0:
        break

print('Sum of digits: %d' % sum)
'''


