num = int(input())

if num >= 100 and num <= 200:
    pass # is used when a block of code is defined and don't want it print anything
else:
    print('Invalid')

# below is the alternative solution, where the pythonic code is more optimised
'''
if not (num >= 100 and num <= 200):
    print('Invalid')
'''