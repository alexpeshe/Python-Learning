speed = float(input())

if speed <= 10:
    print("Slow")
elif 10 < speed <= 50:
    print("Average")
elif 50 < speed <= 150:
    print("Fast")
elif 150 < speed <= 1000:
    print("Ultra Fast")
else:
    print("Extremely Fast")
