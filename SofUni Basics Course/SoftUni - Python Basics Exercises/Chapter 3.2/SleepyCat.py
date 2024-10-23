import math

restdays = int(input())

work_days = 365 - restdays

minutes_to_play = (work_days * 63) + (restdays*127)

difference = math.fabs(minutes_to_play - 30000)
hours = difference // 60
minutes = difference % 60

if minutes_to_play > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more to play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less to play')