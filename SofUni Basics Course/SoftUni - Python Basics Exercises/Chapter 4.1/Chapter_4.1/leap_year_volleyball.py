# leap_year_volleyball.py

year_type = input()#leap or normal
holidays = int(input()) # holidays variable
weekends_home = int(input()) # weekends variable

sofia_weekends = 48 - weekends_home
playing_in_sofia = holidays * (3/4) +  (holidays * (2/3))
playing_total = weekends_home + sofia_weekends

play_total = 0

if year_type == "leap":
    play_total = playing_total * 1.15
elif year_type == "normal":
    play_toral = playing_total

import math

print(math.floor(play_toral))