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

def numberToEnglishText(n):
    if n == 0:
        return 'zero'
    if n < 0:
        return 'negative ' + numberToEnglishText(-n)

    result = ''

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

# Get the number from the user
number = int(input("Enter a number between 0 and 100: "))

# Check if the number is within the valid range
if 0 <= number <= 100:
    # Call the function and print the result
    print(numberToEnglishText(number))
else:
    print("Please enter a number between 0 and 100.")