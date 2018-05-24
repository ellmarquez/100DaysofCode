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

for x in range (0,5):
    guess = input ("Player 2: You can now guess the word or guess a Letter. \n What is your guess?").lower()
    if guess == word:
     print ("YAYA! You win!")
     exit()
    elif guess in (word):
        print (guess + " is in the word!")
### Code above this line works 
    elif guess != word:
        turn=0
        for x in range (0,5):
            ct= 5 - turn
            if guess not in (word):
                turn+=1
                print (guess + " is not in the word!" + str(ct) + " more tries! ")
                if turn==1:
                    from Hangmanboard import head
                    head()
                if turn ==2:
                    from Hangmanboard import body
                    body()
                elif turn ==3:
                    from Hangmanboard import larm
                    larm()
                elif turn ==4: 
                    from Hangmanboard import rarm
                    rarm()
                elif turn ==5: 
                    from Hangmanboard import lleg
                    lleg()
                elif turn ==6:
                    from Hangmanboard import rleg
                    rleg()
            



#elif turn ==5:
          #from Hangmanboard import rleg
          #rleg()   