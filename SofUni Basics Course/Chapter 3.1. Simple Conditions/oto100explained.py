numDic = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred'
}

# a dictionary with the values

'''
Below is  the This line defines a function named numberToEnglishText that takes a number n as input and returns its text representation.
Functions are reusable blocks of code that can be called with different arguments to perform specific tasks.

These lines handle the base cases:
If the input number n is 0, the function returns "zero".
If n is negative, the function recursively calls itself with the absolute value of n and prepends "negative " to the result.
'''


def numberToEnglishText(n):
    if n == 0:
        return 'zero'
    if n < 0:
        return 'negative ' + numberToEnglishText(-n)

    result = ''


''' 
The Main Logic:
This part of the function iterates through the keys of the numDic dictionary in descending order (from 100 to 1).
For each key num, it calculates the quotient of n divided by num (using integer division //).
If the quotient count is greater than or equal to 1:
If num is less than or equal to 20 or 100, it directly appends the corresponding text representation (e.g., "twenty-five" for 25).
Otherwise, it appends the text representation of num and recursively calls numberToEnglishText with the remaining count (e.g., "forty" and "two" for 42).
It updates n by subtracting num * count to handle the remaining part of the number.
The result string is gradually built up by concatenating the text representations of the individual components.
'''

for num in sorted(numDic.keys(), reverse=True):
    count = n // num

    if count >= 1:
        if num <= 20 or num == 100:
            result += numDic[num * count]
        else:
            result += numDic[num]
            if count > 1:
                result += ' ' + numberToEnglishText(count)
        n -= num * count
        if n > 0:
            result += ' '

return result

# Get the number from the user in a form of a variable
number = int(input("Enter a number between 0 and 100: "))

# Check if the number is within the valid range
if 0 <= number <= 100:
    # Call the function and print the result
    print(numberToEnglishText(number))
else:
    print("Please enter a number between 0 and 100.")

    ''' 
this part here 

 checks if the number is within the valid range (0 to 100).
It calls the numberToEnglishText function to get the text representation of the number.
It prints the result if the number is valid, otherwise displays an error message.
    '''