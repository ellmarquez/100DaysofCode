import random
number=random.randint(1,10)
print ("Hello, what is your name?")
name=input()

print ('Hello,' +name, "I am thinking of a number from 1-10, can you guess it?")
guess=int(input())

if guess==number:
      print ("yaya! you got it right!")
elif guess > number:
     print ("To big!")
elif guess < number:
    print("To small!")

print ('Thanks for playing')
