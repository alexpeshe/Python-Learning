# Input: size of the STOP sign
# User provides an integer that determines the height and width of the STOP sign
n = int(input())

# Top line (first row)
# Calculate the number of dots on each side and the number of underscores
dots = n + 1  # Number of dots on each side of the top line
underscores = 2 * n + 1  # Number of underscores in the middle
# Print the top line: dots + underscores + dots
print('.' * dots + '_' * underscores + '.' * dots)

# Upper triangular part
# This loop creates the top slanting part of the STOP sign
for row in range(n):
    # Calculate dots on each side (decreasing as we go down)
    cur_dots = dots - row - 1
    # Calculate underscores (increasing as we go down)
    cur_underscores = underscores + (row * 2)
    
    # Print each row of the upper triangular part
    # Format: dots + '//' + underscores + '\\\\' + dots
    print('.' * cur_dots + '//' + '_' * (cur_underscores - 2) + '\\\\' + '.' * cur_dots)

# Middle line with "STOP!"
# Calculate padding underscores to center "STOP!"
stop_line_underscores = (underscores + (n - 1) * 2 - len("STOP!")) // 2

# Print the middle line with "STOP!" centered
print('//' + '_' * stop_line_underscores + 'STOP!' + '_' * stop_line_underscores + '\\\\')

# Lower triangular part
# This loop creates the bottom slanting part of the STOP sign
for row in range(n):
    # Calculate dots on each side (increasing as we go down)
    cur_dots = row
    # Calculate underscores (decreasing as we go down)
    cur_underscores = underscores + (n - 1) * 2 - (row * 2)
    
    # Print each row of the lower triangular part
    # Format: dots + '\\\\' + underscores + '//' + dots
    print('.' * cur_dots + '\\\\' + '_' * cur_underscores + '//' + '.' * cur_dots)


'''# Input: size of the STOP sign
n = int(input())

# Top line (first row)
dots = n + 1
underscores = 2 * n + 1
print('.' * dots + '_' * underscores + '.' * dots)

# Upper triangular part
for row in range(n):
    cur_dots = dots - row - 1
    cur_underscores = underscores + (row * 2)
    print('.' * cur_dots + '//' + '_' *(cur_underscores -2)+ '\\\\' + '.' * cur_dots)

# Middle line with "STOP!"
stop_line_underscores = (underscores + (n - 1) * 2 - len("STOP!")) // 2
print('//' + '_' * stop_line_underscores + 'STOP!' + '_' * stop_line_underscores + '\\\\')

# Lower triangular part
for row in range(n):
    cur_dots = row
    cur_underscores = underscores + (n - 1) * 2 - (row * 2)
    print('.' * cur_dots + '\\\\' + '_' * cur_underscores + '//' + '.' * cur_dots)
'''
