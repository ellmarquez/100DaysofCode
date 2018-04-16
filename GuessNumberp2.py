import random
print ("Hello, what is your name?")
person=input()

number=random.randint(1,10)
print ('Hello,' ,person, 'I am thinking of a number from 1-10.')

for guess in range (6):
    print('Why don\'t you take a guess?')
    guess= int(input())
    if guess > number:
     print ("To big!")
    elif guess < number:
     print("To small!")
    else:break

if guess ==number:        
    print ('Thats it! Thanks for playing')
else: 
    print('Better luck next time!')
