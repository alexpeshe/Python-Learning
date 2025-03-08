#.strip() doesn't control line printing - it removes leading and trailing whitespace characters from a string. Here's a detailed explanation:

# What .strip() Does:
'''
text = "   hello world   "
print(text.strip())         # Outputs: "hello world"

numbers = "123   "
print(numbers.strip())      # Outputs: "123"
'''

'''
The .strip() method has three variants:

strip(): Removes both leading and trailing whitespace

lstrip(): Removes leading whitespace only

rstrip(): Removes trailing whitespace only

'''
