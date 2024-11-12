# odd_even_sum.py

n = int(input())
odd_sum = 0
even_sum = 0

for number in range (1, n+1):
    current_sum = int(input())
    if number %2 == 0:
        even_sum += current_sum
    else:
        odd_sum += current_sum
    
# Don't ever give up!