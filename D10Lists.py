list=[]
while True:
    print('Enter your item:(Done to quit)')
    item=input()
    list.append(item)
    if item=='Done':
        del list[-1]
        list[-1] = 'and '+list[-1]
        finallist=', '.join(list)
        print(finallist)
        break

