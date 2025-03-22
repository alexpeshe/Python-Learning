# Get input for size of the dress
n = int(input())

# Calculate initial dimensions
width = 5*n              # Total width of the pattern
dots = n                 # Initial number of dots on each side
hashtags = width - dots*2  # Initial number of hashtags in middle

# Draw top section of dress
for i in range(1, n//2+1):
    print('.'*dots + '#'*hashtags + '.'*dots)  # Print pattern
    dots += 1           # Increase dots on each side
    hashtags = width - dots*2  # Recalculate hashtags based on dots
    
"""
Alternative solution of the dependency!
print('.'*(dots+i) +'#'*(hashtags-i*2) + '.'*(dots+i))
"""

# Calculate middle section dimensions
middle_dots = width-2 - 2*dots  # Space between # symbols

# Draw middle section of dress
for i in range(1, n//2+2): 
    print('.'*dots + "#" + '.'*middle_dots + '#' + "."*dots)
    dots += 1           # Increase side dots
    middle_dots -= 2    # Decrease middle dots

# Draw connecting line
print('.'*(dots-1) + '#'*(middle_dots+4) + '.'*(dots-1))

# Calculate bottom section dimensions
hashtags = n+4          # Width of bottom hashtag section
dots = (width - hashtags)//2  # Dots needed on each side

# Draw first part of bottom section
for i in range(1, n//2+1):
    print('.'*dots + '#'*hashtags + '.'*dots)

# Draw DANCE text
static_dots = (width - 10)//2  # Calculate spacing for text
print('.'*static_dots + 'D^A^N^C^E' + '.'*static_dots)

# Draw final part of bottom section
for i in range(1, n//2+2):
    print('.'*dots + '#'*hashtags + '.'*dots)

"""
Alternative solution of the dependency!
print('.'*(dots+i) +'#'*(hashtags-i*2) + '.'*(dots+i))
"""

'''
Pattern Components
Top section: Wide hashtag band that narrows

Middle section: Two parallel lines getting further apart

Connecting line: Single line connecting parallel lines

Bottom section: Consistent width band

DANCE text: Centered text

Final section: Matching bottom band

Key Points
Uses multiplication for pattern repetition

Calculations depend on initial input 'n'

Pattern is symmetrical

Uses dots (.) and hashtags (#) for design

'''

"""
Function version:

def validate_input(n):
    Validates if input is even and positive
    if n <= 0 or n % 2 != 0:
        print("Please enter a positive even number")
        return False
    return True

def draw_top(n, width):
    Draws top section of dress
    for i in range(n // 2):
        dots = n - i
        hashtags = width - 2 * dots
        print('.' * dots + '#' * hashtags + '.' * dots)

def draw_middle(n, width):
    Draws middle section with parallel lines
    for i in range(n // 2 + 1):
        dots = n - i
        middle_dots = width - 2 - 2 * dots
        print('.' * dots + '#' + '.' * middle_dots + '#' + '.' * dots)
    
    # Connecting line
    print('.' * (dots - 1) + '#' * (middle_dots + 4) + '.' * (dots - 1))

def draw_bottom(n, width):
    Draws bottom section of dress
    hashtags = n + 4
    dots = (width - hashtags) // 2
    
    # First bottom part
    for i in range(n // 2):
        print('.' * dots + '#' * hashtags + '.' * dots)
    
    # DANCE text
    static_dots = (width - 10) // 2
    print('.' * static_dots + 'D^A^N^C^E' + '.' * static_dots)
    
    # Final bottom part
    for i in range(n // 2 + 1):
        print('.' * dots + '#' * hashtags + '.' * dots)

def draw_dress(n):
    Main function to draw the entire dress
    if not validate_input(n):
        return
        
    width = 5 * n
    draw_top(n, width)
    draw_middle(n, width)
    draw_bottom(n, width)

# Example usage
n = 6  # Can be replaced with input(): n = int(input())
draw_dress(n)
"""