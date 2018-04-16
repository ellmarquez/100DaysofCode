
## abs() fir absolute value ex: the absolute value of 15 is 15 but -74 is 74
print ('Learing about abs')
miles_from_origin = 10 
miles_traveled = 50

miles_to_go = miles_from_origin - miles_traveled
print(miles_to_go)
print(abs(miles_to_go)) #use absolute value to account for negative number

## divmod() to find a quotient and remainder simultaneously
## divmod(a,b)
print('\nLearing about divmod')
words = 80000
per_page_A=300 #option A, 300 words per page
per_page_B= 250 #option B, 25 words per page
print (divmod(words,per_page_A), ('words per page'))
print (divmod(words,per_page_B),('words per page'))

## pow() to raise a number to a certain power instead of **
print('\n')
print ('now lets learn about pow!')
hours =24
total_bacteria =pow(2,hours)
print(total_bacteria)


## round() to round a number to a certain decimal point
print ('\nRounding')
i=3.3335
print (round(i,4),'\n')
## sum() to calculate the sum of the items in an iterable data type

#Python will add a new Line character at the end of you print function.
print( 'Shall we take a break?')
print ('hello')
print ('world')

print ('Hello', end='')
print ('world')

print('Hello', 'World')
print('Hello','World',sep=',')


