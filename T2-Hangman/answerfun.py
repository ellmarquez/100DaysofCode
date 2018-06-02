def correct():
    if guess in SecureWord:
            for (location, character) in enumerate(SecureWord):
                if character==guess:
                    print (guess +" is located in position: " + str(location))
                    SecureList[location]=guess 
            print (str(SecureList))
            if SecureList == SecureWord:
                print ("YAYA! You Win! The word was " +str(word) +".")
                exit()