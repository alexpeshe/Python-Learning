# Tips for solving the task
# row is even (n-2)//2 gives us the stars
# for rows in range(0, to the rows)
# for row in range(0, int(my_range))
# if col.rows are even n - 1
# if uneven n

n = int(input())

# Upper half of the diamond (including middle row)
for row in range(n // 2 + 1):
    # Calculate dashes on each side
    dash_count = abs(n // 2 - row)
    
    # Calculate star count
    if row <= n // 2:
        star_count = 2 * row + 1
    else:
        star_count = 2 * (n - row - 1) + 1
    
    # Calculate inner space
    inner_space = max(0, star_count - 2)
    
    # Print the row
    if star_count == 1:
        # Middle row with single star
        print('-' * dash_count + '*' + '-' * dash_count)
    else:
        # Rows with two stars and inner space
        print('-' * dash_count + '*' + '-' * inner_space + '*' + '-' * dash_count)

# Lower half of the diamond
for row in range(n // 2 - 1, -1, -1):
    # Calculate dashes on each side
    dash_count = abs(n // 2 - row)
    
    # Calculate star count
    if row <= n // 2:
        star_count = 2 * row + 1
    else:
        star_count = 2 * (n - row - 1) + 1
    
    # Calculate inner space
    inner_space = max(0, star_count - 2)
    
    # Print the row
    if star_count == 1:
        # Middle row with single star
        print('-' * dash_count + '*' + '-' * dash_count)
    else:
        # Rows with two stars and inner space
        print('-' * dash_count + '*' + '-' * inner_space + '*' + '-' * dash_count)






