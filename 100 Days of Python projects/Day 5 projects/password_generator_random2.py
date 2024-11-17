import random

# Define the character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Hard Version (Step 2)
# When you've completed the easy version, you're ready to tackle the hard version. 
# In the advanced version of this project the final password does not follow a pattern. 
# So the example above might look like this:

# Create an empty password list
password_list = []

# Add letters to the password
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add symbols to the password
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add numbers to the password
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list to randomize the order
random.shuffle(password_list)

# Convert the list to a string
password = ''

# loop through the random list
for c in password_list:
    password += c

print(f"Password for easy level: {password}")