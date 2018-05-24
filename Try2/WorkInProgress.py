#! /usr/local/bin/python3
import os

word= input ("Player 1: Please enter the word!").lower()
lw= len(word)
#os.system('clear')

### Hands off to Player 2 
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
### To do: add visible counter for user
### Code above this line works 

guess = input ("Player 2: You can now guess the word or guess a Letter. \n What is your guess?").lower()
if guess == word:
    print ("yaya you win!")
    exit()
elif guess != word:
    for turn in range (1,6):
        if guess in (word):
            print (guess + " is in the word!")        
        elif guess not in (word):
            turn+=1
            print (guess + " is not in the word!")
            if turn==1:
              from Hangmanboard import head
              head()
            elif turn ==2:
                from Hangmanboard import body
                body()
            elif turn ==3:
                from Hangmanboard import larm
                larm()
  
            



elif turn ==5:
          from Hangmanboard import rleg
          rleg()   