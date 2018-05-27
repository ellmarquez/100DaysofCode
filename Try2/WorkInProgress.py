#! /usr/local/bin/python3
import os 
import time

SecureWord=[]
word= input ("Player 1: Please enter the word!").lower()
lw= len(word)
SecureWord=list(word)
os.system('clear')
print ("You can now pass keyboard to player 2.")
for i in range(5,0,-1):
    time.sleep(1)
    print (i)
#time.sleep(5)
os.system('clear')

### add a wait time for passing to player2 

print (""" Welcome to Hangman!  
             +---+
             |
             |
             |
             |
             ======= 
             
              """)
print("The word has " + str(lw) + " letters.")
print ("_ "*len(word))

### Decouple this section for guess function/class 
turn =0
while turn < 6:
    guess = input ("Player 2: You can now guess the word or guess a Letter. \n What is your guess?").lower()
    if guess == word:
     print ("YAYA! You win!")
     exit()
    elif guess in SecureWord:
            print (guess +" is located in position: " + str(SecureWord.index(guess)))
                
## what about multiple letters?
    else:
        print (guess + " is not in the word!")
        turn+=1
        if turn==1:
            from Hangmanboard import head
            head()
        elif turn ==2:
            from Hangmanboard import body
            body()
        elif turn ==3:
            from Hangmanboard import rarm
            rarm() 
        elif turn ==4: 
            from Hangmanboard import larm
            larm()
        elif turn ==5: 
            from Hangmanboard import lleg
            lleg()
        elif turn ==6:
            from Hangmanboard import rleg
            rleg()
            
 