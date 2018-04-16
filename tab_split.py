print('How much was your bill?' )
bill=float(input())
print('How much would you like to tip?')
tip=.15
split=3

total= bill + (bill*tip)
each_pay = total/split
print('Each person pays',(each_pay))
print('But we can\'t split pennies; so we can pay:', round(each_pay,2)) #round  the number 