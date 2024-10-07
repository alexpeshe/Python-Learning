bitcoin = int(input())
yuan = float(input())
commission = float(input()) / 100
print(commission)

bitcoin_lev = bitcoin * 1168
print(bitcoin_lev)

usd_yuan = 0.15*yuan
print(usd_yuan)

usd_to_lev = usd_yuan*1.76
print(usd_to_lev)

euros = (bitcoin_lev + usd_to_lev) / 1.95

euros_commission = euros * commission
print(euros_commission)

final_euros = (euros - euros_commission)

print("%.2f" % final_euros)
