import datetime
from datetime import datetime
from datetime import timedelta

now = datetime.now() # Calculating or calling the date and time now

DOB = input("Enter a date (YYYY-MM-DD): ")
user_date = datetime.strptime(DOB, "%Y-%m-%d")
# Create=ing a date variable from user input:

future_date = user_date + timedelta(days=1000)
print(f"The date 1000 days from {DOB} is: {user_date}")
print("The date and time now is " + str(now))


