# A simple program to print out the maxi input from a user
# Thanks for using

number1 = int(input('what is your first number'))
number2 = int(input('what is your second number?'))
number3 = int(input('what is your third number?'))
number4 = int(input('what is your fourth number'))
number5 = int(input('what is your fifth number'))

maxi = number1
if number2 > maxi:
    maxi = number2
if number3 > maxi:
    maxi = number3
if number4 > maxi:
    maxi = number4
if number5 >maxi:
    maxi = number5
print('The max number is ' + str(maxi))
