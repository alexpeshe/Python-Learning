def print_diamond():
    """
    Advanced diamond printing with multiple customization options
    """
    while True:
        try:
            # Comprehensive input options
            print("\n--- Diamond Customization ---")
            n = int(input("Enter diamond size: "))
            
            # Validate input
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            
            # Character selection
            char = input("Enter character (default '*'): ") or '*'
            
            # Color selection (optional)
            colors = {
                'red': '\033[91m',
                'green': '\033[92m',
                'blue': '\033[94m',
                'yellow': '\033[93m',
                'default': '\033[0m'
            }
            
            print("\nAvailable colors:")
            for color in colors.keys():
                print(f"- {color}")
            
            color_choice = input("Choose a color (default is no color): ").lower()
            color = colors.get(color_choice, colors['default'])
            
            # Diamond printing
            for i in range(n):
                print(color + ' ' * (n - i - 1) + char * (2 * i + 1) + colors['default'])
            
            for i in range(n - 2, -1, -1):
                print(color + ' ' * (n - i - 1) + char * (2 * i + 1) + colors['default'])
            
            # Continuation
            another = input("\nPrint another diamond? (yes/no): ").lower()
            if another != 'yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Call the function
print_diamond()


'''
Alternative version:

def print_diamond():
    # Prompt user to input the size of the diamond
    while True:
        try:
            # Get input and convert to integer
            n = int(input("Enter the size of the diamond (must be a positive integer): "))
            
            # Validate input
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            
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
            
            # Ask if user wants to continue
            another = input("Do you want to print another diamond? (yes/no): ").lower()
            if another != 'yes':
                break
        
        except ValueError:
            # Handle invalid input (non-integer)
            print("Invalid input. Please enter a valid integer.")

# Call the function
print_diamond()

Alternative 2:

def print_diamond(character='*'):
    """
    Print a diamond pattern with customizable options
    
    Parameters:
    - character: Character to use for drawing the diamond (default is '*')
    """
    while True:
        try:
            # Get diamond size input
            n = int(input("Enter the size of the diamond: "))
            
            # Validate input
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            
            # Optional: Allow custom character
            custom_char = input("Enter a character to use (press Enter for default '*'): ") or character
            
            # Upper half of diamond (including middle line)
            for i in range(n):
                # Calculate and print leading spaces
                print(' ' * (n - i - 1), end='')
                
                # Calculate and print characters
                print(custom_char * (2 * i + 1))
            
            # Lower half of diamond
            for i in range(n - 2, -1, -1):
                # Calculate and print leading spaces
                print(' ' * (n - i - 1), end='')
                
                # Calculate and print characters
                print(custom_char * (2 * i + 1))
            
            # Continuation prompt
            another = input("Do you want to print another diamond? (yes/no): ").lower()
            if another != 'yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Call the function
print_diamond()
'''

'''
Key Improvements:

Input Validation

Checks for positive integers
Handles non-integer inputs
User Interaction

Allows multiple diamond prints
Option to customize character
Continuation prompt
Error Handling

Try-except blocks
Prevents program crash
Guides user to correct input
Flexibility

Works with different sizes
Customizable characters
Optional color (in advanced version)
Recommendations:

Start with the basic version
Gradually add features
Test with various inputs
Handle edge cases
Would you like me to elaborate on any part of the code or explain the concepts in more detail?
'''