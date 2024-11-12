
word = input()

a = 1
e = 2
i = 3
o = 4
u = 5

sum = 0 

for l in word.lower(): # stands for letter
    if l == 'a':
        sum += a
    elif l == 'e':
        sum += e
    elif l == 'i':
        sum += i
    elif l == 'o':
        sum += o
    elif l == 'u':
        sum += u

print(sum) # prints the sum of the letters in the word

# Решението на SoftUni

''' 
str = input().lower()
sum = 0

for c in str:
    if c == 'a':
        sum += 1
    elif c == 'e':
        sum += 2

        и т.н. '''
