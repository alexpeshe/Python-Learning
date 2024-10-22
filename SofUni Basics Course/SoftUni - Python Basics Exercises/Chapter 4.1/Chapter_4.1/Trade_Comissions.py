town = input()
sales = float(input())
# above are the two main variables

result = 'error' # 0 # changing variable which is very useful
# if the result is set to error by default the last logical or at the end of the program
# isn't really needed!

if town == 'Sofia': # this is the main if construction and below are the nested ifs
    if sales >= 0 and sales <= 500:
        result = sales * 0.05 # the default error in result gets changed to a number.

    elif sales > 500 and sales <= 1000:
        result = sales * 0.07

    elif sales > 1000 and sales <= 10000:
        result = sales * 0.08

    elif sales > 10000:
        result = sales * 0.12

elif town == 'Plovdiv':
    if sales >= 0 and sales <= 500:
        result = sales * 0.055

    elif sales > 500 and sales <= 1000:
        result = sales * 0.08

    elif sales > 1000 and sales <= 10000:
        result = sales * 0.12

    elif sales > 10000:
        result = sales * 0.145

elif town == 'Varna':
    if sales >= 0 and sales <= 500:
        result = sales * 0.045

    elif sales > 500 and sales <= 1000:
        result = sales * 0.075

    elif sales > 1000 and sales <= 10000:
        result = sales * 0.10

    elif sales > 10000:
        result = sales * 0.13

else:
    result = 'error'
   #if result == 'error':
        #print('error')

#print("{:.2f}".format(result))
# above is the alternative solution to the solution below.

if type(result) == str # or sales < 0: # avoiding a zero error
    # print('error')
    print(result) # result it set to error and by default is changing
else:
    print("{:.2f}".format(result))
# formating the result to two decimal points

