tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    for i in table:
        for x in range(i):
            print (x)
        #c=(str(' '.join(i)))
       # print (c.rjust(y))

printTable(tableData)  