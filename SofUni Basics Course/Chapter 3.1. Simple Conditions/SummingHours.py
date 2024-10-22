hours = int(input())
minutes = int(input())
extra = 15

extra_minutes = minutes + extra

# Ако минутите са повече от 59, добавяме 1 час и изваждаме 60 минути
if hours < 24:
    print(str(hours) + ":0" + str(extra_minutes))

