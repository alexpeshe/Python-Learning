days = int(input())
daily_earnings = float(input())
usd_lev = float(input())
tax = 0.25

monthly_salary = days * daily_earnings
print("Montlh earnings: ", monthly_salary)

yearly_earnings = (monthly_salary * 12) + (monthly_salary *2.5)
print("Yearly earnings: ", yearly_earnings)

taxes_paid = yearly_earnings * tax
print("Yearly tax is: ", taxes_paid)

earnings_after_tax = yearly_earnings - taxes_paid
print("Yearly earnings after tax is: ", earnings_after_tax)

earnings_lev = earnings_after_tax * usd_lev
print("Lev earnings: ",  earnings_lev)

avg_daily_eearning = earnings_lev/365
print("AVG daily earnings: " "%.2f" % avg_daily_eearning)


