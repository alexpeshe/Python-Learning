n = int(input())

# We use 10000 because range() excludes the last number
# Keep in mind the difference between operators for integer division // and division with remainder % in Python.
# Get input number that we'll use to check divisibility
# Initialize empty string to store special numbers

result = ''

# Loop through all 4-digit numbers (1111 to 9999)
for number in range(1111, 10000):
    # Convert the current number to string to access individual digits
    number_as_string = str(number)    # Example: 1234 becomes "1234"
    
    # Print current number and its digits
    print(number, end=" ")   # end=" " prevents new line
    
    # Loop through each character (digit) in the string
    for digit in number_as_string:    # Example: "1", "2", "3", "4"
        print(digit, end=" ")         # Print each digit with space
    
    print()  # Add new line after printing all digits

