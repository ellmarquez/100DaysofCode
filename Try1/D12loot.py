BagOfHolding={'rope':1, 'tourch':6 , 'gold coin':42, 'dagger':1, 'arrow': 12}
dragonLoot=['gold coin','gold coin', 'dagger', 'gold coin', 'ruby']
#addToInventory(inventory, additem)

def displayInventory(BagOfHolding):
    print ('Your inventory includes the following:' )
    item=0
    for k, v in BagOfHolding.items():
        print (k,v)
        item = item + v
    print('Your total inventory includes: '+ str(item) + ' items')

def addToInventory(inventory, additem):
    for i in additem:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i] + 1
    return inventory


newloot= addToInventory(BagOfHolding, dragonLoot)   
displayInventory (newloot)    
        
    

