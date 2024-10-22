# leap_volleyball2.py

# Read input
year_type = input().lower()  # leap or normal
holidays = int(input())      # number of holidays
weekends_home = int(input()) # number of weekends Vladimir travels home

# Calculate playing days
# 1. Games in Sofia during weekends
weekends_in_sofia = 48 - weekends_home  # total weekends minus weekends at home
playing_weekends_sofia = weekends_in_sofia * (3/4)  # he plays 3/4 of the weekends in Sofia

# 2. Games during holidays
playing_holidays = holidays * (2/3)  # he plays 2/3 of the holidays

# 3. Games when visiting hometown
playing_hometown = weekends_home  # he plays every Sunday when at hometown

# Calculate total games
total_playing_days = playing_weekends_sofia + playing_holidays + playing_hometown

# Adjust for leap year
if year_type == "leap":
    total_playing_days += total_playing_days * 0.15

# Round down to nearest integer
result = int(total_playing_days)

print(result)