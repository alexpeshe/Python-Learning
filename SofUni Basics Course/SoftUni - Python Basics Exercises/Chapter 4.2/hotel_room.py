# My solution

# Get user input for month and number of stays
month = input()  # Input for month (May, June, July, August, September, October)
stays = int(input())  # Number of nights as integer

# Initialize variables for calculations and output
result = ""  # Store the final formatted output string
studio = 0   # Base price for studio room
apartment = 0  # Base price for apartment
studio_price = 0  # Final price for studio after discounts
apartment_price = 0  # Final price for apartment after discounts

# Set base prices based on the month
if month == "May" or month == 'October':
    studio = 50
    apartment = 65
elif month == "June" or month == 'September':
    studio = 75.2
    apartment = 68.7
elif month == "July" or month == 'August':
    studio = 76
    apartment = 77

# Calculate final prices with discounts for May and October
if month == "May" or month == 'October':
    if stays <= 7:  # Up to 7 nights: 5% discount on studio
        studio_price = stays * (studio - (studio * 0.05))
        result = f" Studio {abs(studio_price):.2f}lv"
    elif 7 > stays <= 14:  # 8-14 nights: 30% discount on studio
        studio_price = stays * (studio - (studio * 0.3))
        result = f" Studio {abs(studio_price):.2f}lv"
        studio_price = stays * (studio - (studio * 0.2))
        apartment_price = stays * (apartment - (apartment * 0.1))
        result = f"Apartment {abs(apartment_price):.2f} lv \
              Studio {abs(studio_price):.2f} lv"   

# Print the final result
print(result)

'''
Claude's improved Solution 

# Get input from user
month = input()  # Get the month (May, June, July, August, September, October)
stays = int(input())  # Get number of stays as integer

# Initialize variables
result = ""  # Empty string to store the final formatted output
studio = 0   # Base price for studio
apartment = 0  # Base price for apartment
studio_price = 0  # Will store final studio price after discounts
apartment_price = 0  # Will store final apartment price after discounts

# Set base prices according to month
if month == "May" or month == 'October':
    studio = 50
    apartment = 65
elif month == "June" or month == 'September':
    studio = 75.20
    apartment = 68.70
elif month == "July" or month == 'August':
    studio = 76
    apartment = 77

# Calculate prices with discounts based on month and length of stay
if month == "May" or month == 'October':
    if stays <= 7:  # For stays up to 7 nights
        studio_price = stays * studio
        apartment_price = stays * apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."
    elif 7 < stays <= 14:  # For stays between 8 and 14 nights
        studio_price = stays * (studio - (studio * 0.05))  # 5% discount on studio
        apartment_price = stays * apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."
    else:  # For stays more than 14 nights
        studio_price = stays * (studio - (studio * 0.30))  # 30% discount on studio
        apartment_price = stays * (apartment - (apartment * 0.10))  # 10% discount on apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."
elif month == "June" or month == 'September':
    if stays <= 14:  # For stays up to 14 nights
        studio_price = stays * studio
        apartment_price = stays * apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."
    else:  # For stays more than 14 nights
        studio_price = stays * (studio - (studio * 0.20))  # 20% discount on studio
        apartment_price = stays * (apartment - (apartment * 0.10))  # 10% discount on apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."
elif month == "July" or month == 'August':
    if stays <= 14:  # For stays up to 14 nights
        studio_price = stays * studio
        apartment_price = stays * apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."
    else:  # For stays more than 14 nights
        studio_price = stays * studio
        apartment_price = stays * (apartment - (apartment * 0.10))  # 10% discount on apartment
        result = f"Apartment {apartment_price:.2f} lv.\nStudio {studio_price:.2f} lv."

# Print final result
print(result)
'''