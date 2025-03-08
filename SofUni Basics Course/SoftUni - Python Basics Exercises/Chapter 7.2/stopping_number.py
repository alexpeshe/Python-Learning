n = int(input())
m = int(input())
s = int(input())

result = ''  # Use string to collect results

for i in range(m, n-1, -1):
    if i % 2 == 0 and i % 3 == 0:  # Check both conditions together
        if i == s:                  # Check stop number
            break
        result += str(i) + ' '      # Add number to result string

print(result.strip())               # Print all numbers on one line


'''
Key points in this solution:

Input Handling:

We read three integers: n (start), m (end), and s (stop number)

The range should be n ≤ number ≤ m

Loop Structure:

Use range(m, n-1, -1) to loop in reverse order

Start from m (highest)

Go down to n (lowest)

Step of -1 to go backwards

Divisibility Check:

Use i % 2 == 0 and i % 3 == 0 to check if number is divisible by both 2 and 34

This is more efficient than using division (//)

Stop Number Check:

Break the loop if current number equals stop number

This ensures we stop printing when we hit the stop number

Output Formatting:

Build string with spaces between numbers

Use strip() to remove trailing space

Numbers are automatically in reverse order due to loop structure

This solution will produce the expected output for all your test cases. For example:

Input: 1, 30, 15 → Output: 30 24 18 12 6

Input: 1, 36, 12 → Output: 36 30 24 18
'''