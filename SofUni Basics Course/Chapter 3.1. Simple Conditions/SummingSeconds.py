first = int(input())
second = int(input())
third = int(input())

sum = first + second + third

minutes = sum // 60

seconds = minutes % 60

if seconds < 10:
    print(str(minutes) + ":0" + str(seconds))
else:
    print(str(minutes) + ":" + str(seconds))



