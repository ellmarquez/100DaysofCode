#! /usr/local/bin/python3
import os

word= input ("Player 1: Please enter the word!").lower()
lw= len(word)
#os.system('clear')

print (""" Welcome to Hangman!  
             +---+
             |
             |
             |
             |
             ======= 
             
              """)
print("The word has " + str(lw) + " letters.")

for x in range (0,5):
    turn=0
    guess = input ("Player 2: You can now guess the word or guess a Letter. \n What is your guess?").lower()
    if guess == word:
        print ("yaya you win!")
        break
    elif guess in (word):
        print (guess + " is in the word!")
        
    elif guess not in (word):
        turn+=1
        print (guess + " is not in the word!")
        if turn ==1:
            from Hangmanboard import head
            head()
        elif turn ==2:
            from Hangmanboard import body
            body()
        elif turn ==3:
            from Hangmanboard import larm
            larm()
    else:
        from Hangmanboard import rleg
        rleg()
            

