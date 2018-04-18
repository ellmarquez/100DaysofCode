birthdays ={'Ell': 'April 1', 'Alice':'Dec 10', 'Jessica':'March 10'}
while True:
    print('Enter a name:(blank to quit)')
    name = input()
    if name=='':
     break
     
    if name in birthdays:
      print (birthdays[name]+'is the birthday of ' + name)
    else:
        print('I do not have birthday information for '+name)
        print('what is their birthday?')
        birthday=input()
        birthdays[name]=birthday
        print ('birthday database updated')