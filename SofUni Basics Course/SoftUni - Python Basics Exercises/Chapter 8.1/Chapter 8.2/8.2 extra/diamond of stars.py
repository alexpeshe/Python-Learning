def print_diamond(n):
    # Convert input to integer
    n = int(n)
    
    # Upper half of diamond (including middle line)
    for i in range(n):
        # Calculate and print leading spaces
        print(' ' * (n - i - 1), end='')
        
        # Calculate and print stars
        print('*' * (2 * i + 1))
    
    # Lower half of diamond
    for i in range(n - 2, -1, -1):
        # Calculate and print leading spaces
        print(' ' * (n - i - 1), end='')
        
        # Calculate and print stars
        print('*' * (2 * i + 1))

# Get input from user
size = input("Enter the size of the diamond: ")
print_diamond(size)
