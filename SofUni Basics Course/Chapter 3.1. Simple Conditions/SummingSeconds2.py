sec1 = int(input())
# TODO: Read also sec2 and sec3 ...
secs = sec1 + sec2 + sec3
mins = 0

if secs › 59:
# TODO: Repeat this 2 times ...
    mins++;
    secs = secs - 60
if secs ‹ 10:
    print(str(mins) + ":" + '0' + str(secs))
else:
    print(str(mins) + ':' ++ str(seconds))



