n = int(input())
l = int(input())

start_letter = 97 # use ASCII table
end_letter = start_letter+l

for num1 in range(1, n):
    for num2 in range(1, n):
        for num3 in range(start_letter, end_letter):
            for num4 in range(start_letter, end_letter):
                for num5 in range(1, n+1):
                    if num5>num1 and num5>num2:
                        print(str(num1)+ str(num2)+chr(num3) +chr(num4)+str(num5), end=' ' + '')

