
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    column_width=[]
    row=len(table[0])
    column=len(table)
    #print (row, column)
   
    for col in table:
        ItemWidth=[]
        for x in col:
            ItemWidth.append(len(x))
            #print (ItemWidth)  
        column_width.append(max(ItemWidth))
    #print(column_width)

    for item in range(row):
        output=[]
        for col in range(column):
            output.append(table[col][item].rjust(column_width[col]))
        print(" ".join(output))


printTable(tableData)
