def triangle(symbol, height):
    for r in range(1, height + 1):
        print(symbol * r)

triangle("*", 9)

''' for r in range(1, height + 1):
This starts a loop that will run 'height' number of times.
r will take values from 1 to 'height' (inclusive).
For example, if height is 9, r will take values 1, 2, 3, ..., 9.

print(symbol * r)
In each iteration of the loop, this line prints the 'symbol' repeated 'r' times.
The * operator, when used with a string and an integer, repeats the string that many times.

For example, if symbol is "" and r is 3, it will print "**".
triangle("*", 9)
This line calls the function with "*" as the symbol and 9 as the height. '''
