import random
print ("Hello, what is your name?")
person=input()

number=random.randint(1,10)
print ('Hello,' ,person, 'I am thinking of a number from 1-10.')

for guesstaken in range (6):
    print('Why don\'t you take a guess?')
    guess= int(input())
    if guess > number:
     print ("To big!")
    elif guess < number:
     print("To small!")
    else:break

if guess ==number:        
    print ('Thats it! Wow it only took you' + str(guesstaken) + ' guesses.' )
else: 
    print('Better luck next time!')
