def print_pyramid(n):
    for i in range(n):
        # Print spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('*' * (2 * i + 1))

# Example usage
print_pyramid(5)