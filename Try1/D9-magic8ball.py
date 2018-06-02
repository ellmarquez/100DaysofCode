import random
messages = ('It is certain', 'It is decidedly so', 'Yes definitely','Reply hazy try again',
'ask again later','Concentrate and ask again', 'NO!', 'Outlook is not so good', 'Very doubtful')

print(messages[random.randint(0,len(messages)-1)])
#produces random number to use for index. The number will be determined by the length of the list
