def create_pattern(size, pattern_config=None):
    """
    Creates a customizable pattern based on the given size and configuration.
    
    Args:
        size: Integer determining the pattern size
        pattern_config: Dictionary with pattern configuration (optional)
    
    Returns:
        List of strings representing the pattern lines
    """
    # Default configuration if none provided
    if pattern_config is None:
        pattern_config = {
            'border': '-',
            'left_edge': '-',
            'right_edge': '-',
            'body_pattern': '\\/',
            'border_multiplier': 2,
        }
    
    # Initialize list to store pattern lines
    pattern_lines = []
    
    # Create the border line (used for top and bottom)
    border = pattern_config['border'] * (size * pattern_config['border_multiplier'])
    
    # Add top border
    pattern_lines.append(border)
    
    # Create body lines
    body_repeat = size - 1  # Number of pattern repetitions
    
    # Using a while loop instead of for loop for the body
    line_count = 1
    while line_count < size - 1:
        # Construct each body line with left edge, pattern, and right edge
        body_line = (
            pattern_config['left_edge'] + 
            pattern_config['body_pattern'] * body_repeat + 
            pattern_config['right_edge']
        )
        pattern_lines.append(body_line)
        line_count += 1
    
    # Add bottom border
    pattern_lines.append(border)
    
    return pattern_lines

def print_pattern(pattern_lines):
    """
    Prints each line in the pattern.
    
    Args:
        pattern_lines: List of strings representing the pattern
    """
    for line in pattern_lines:
        print(line)

def interactive_pattern_creator():
    """
    Interactive function that allows users to customize and create patterns.
    """
    try:
        # Get pattern size
        size = int(input("Enter pattern size: "))
        
        # Offer customization options
        custom = input("Do you want to customize the pattern? (y/n): ").lower()
        
        if custom == 'y':
            # Dictionary for custom configuration
            config = {}
            config['border'] = input("Enter border character (default '-'): ") or '-'
            config['left_edge'] = input("Enter left edge character (default '-'): ") or '-'
            config['right_edge'] = input("Enter right edge character (default '-'): ") or '-'
            config['body_pattern'] = input("Enter body pattern (default '\\/'): ") or '\\/'
            
            try:
                config['border_multiplier'] = int(input("Enter border multiplier (default 2): ") or '2')
            except ValueError:
                config['border_multiplier'] = 2
                print("Invalid multiplier. Using default value 2.")
            
            # Create and print custom pattern
            pattern = create_pattern(size, config)
        else:
            # Create and print default pattern
            pattern = create_pattern(size)
        
        print("\nGenerated Pattern:")
        print_pattern(pattern)
        
        # Offer to save the pattern
        save = input("\nDo you want to save this pattern to a file? (y/n): ").lower()
        if save == 'y':
            filename = input("Enter filename (default 'pattern.txt'): ") or 'pattern.txt'
            with open(filename, 'w') as file:
                for line in pattern:
                    file.write(line + '\n')
            print(f"Pattern saved to {filename}")
            
    except ValueError:
        print("Invalid input. Please enter a valid number for the pattern size.")

# Run the program
if __name__ == "__main__":
    # Simple usage
    size = int(input())
    pattern = create_pattern(size)
    print_pattern(pattern)
    
    # Uncomment to use the interactive version
    # interactive_pattern_creator()

"""
Key Points and Explanations:
------------------------------------------------
Dictionary for Configuration:

Uses a dictionary to store pattern configuration

Makes the pattern highly customizable

Provides default values for optional parameters

Function Design:

create_pattern() generates the pattern but returns it as a list instead of printing directly

print_pattern() handles the display logic separately

Follows the principle of separation of concerns

While Loop Alternative:

Demonstrates using a while loop instead of a for loop

Shows how to track iteration with a counter variable

Achieves the same result with different loop structure

Error Handling:

Try-except blocks catch invalid inputs

Provides meaningful error messages

Falls back to default values when needed

Interactive Features:

interactive_pattern_creator() allows users to customize patterns

Shows how to build an interactive command-line interface

Demonstrates input validation and default values

File I/O Operations:

Offers functionality to save patterns to files

Shows how to write strings to a file

Demonstrates basic file handling

Modular Design:

Each function has a single responsibility

Functions are reusable and composable

Code is organized in a logical manner

String Manipulation:

Demonstrates various string operations

Shows how to build complex strings from components

Uses string multiplication for repeating patterns

Mathematical Logic:

Calculates pattern dimensions based on input size

Shows how to derive values for string repetition

Simplifies complex expressions

This alternative implementation not only reproduces the original pattern but extends it with customization options, better code organization, and additional features like file saving, showcasing more advanced Python concepts and programming practices."""