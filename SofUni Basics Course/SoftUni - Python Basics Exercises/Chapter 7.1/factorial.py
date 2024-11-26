n = int(input()) 

fact = 1

while True:
    fact *= n
    n -= 1
    if not n>1:
        break


'''
alternative solution:
result = 1 # променливата е много важно да не е нула за да се умножава само по себеси


for num in range(n,0, -1):
    result *= num # this is python's so called sugar syntax eaquating to result = result*num

print(num) # printing the end result outside the loop
'''
