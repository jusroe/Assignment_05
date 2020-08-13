#------------------------------------------#
# Title: CDInventory.py (For Assignment05)
# Desc: Script CDINventory to store CD Inventory data and allow user to make changes
# Change Log: (Who, When, What)
# JRoe, 2020-Aug-10, Created file
# JRoe, 2020-Aug-11, Modified code, added annotations
# JRoe, 2020-Aug-12, Modified code, added annotations
#------------------------------------------#

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicrow = {}  # Create dictonary
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
 

# Start script, initiate while loop
print()
print('The Magic CD Inventory\n')
while True:
   #Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

 
    # Exit script
    if strChoice == 'x':
        break
    
    # use 'r' to read data from CDInventory.txt
    # Need to figure out way to tell user if no file with that name exists!
    if strChoice == 'l':
        print('______________Current Inventory______________', '\n\n', 'ID, CD Title, Artist', '\n')
        objFile = open(strFileName, 'r')
        for row in objFile:
            listrow = row.strip().split(',')
            dicrow = {'ID': int(listrow[0]), 'CD Title': listrow[1], 'Artist': listrow[2]}
            lstTbl.append(dicrow)
            strRow = ''
            for item in row:
                strRow += str(item) 
            strRow = strRow[:-1] + '\n'
            print(strRow)
        objFile.close()
        
        
    # Adds entries every time user asks - prevents user from entering ID values that already exist
    elif strChoice == 'a':  
        strID = input('Enter an ID: ')
        try:
            val = int(strID)
        except ValueError:
            print()
            print('Integers Only!')
            print()
            continue
        intID = int(strID)
        for entry in range(len(lstTbl)):
            if lstTbl[entry]['ID'] == intID:
                intID = 'new'
                break
        if intID == 'new':
            print()
            print('This ID has already been used!')
            print()
        else:   
            strTitle = input('Enter the CD\'s Title: ')
            strArtist = input('Enter the Artist\'s Name: ')
            dictrow = {'ID': intID,'Title': strTitle,'Artist': strArtist}
            lstTbl.append(dictrow)
            print()
       
        
    # Displays data saved in memory, utilizes "*" to format row
    elif strChoice == 'i':
        print('ID, CD Title, Artist')
        print('____________________')
        print()
        for row in lstTbl:
            print(*row.values(), sep = ', ')
            print()
    
    
    # Deletes rows selected by the user 
    elif strChoice == 'd':
        print('ID, CD Title, Artist')
        print('____________________')
        print()
        for row in lstTbl:
            print(*row.values(), sep = ', ')
        delete = input('See curent Inventory above - enter ID Number of entry to be deleted: ')
        try:
            val = int(delete)
        except ValueError:
            print()
            print('Integers Only!')
            print()
            continue
        intdelete = int(delete)
        for entry in range(len(lstTbl)):
            if lstTbl[entry]['ID'] == intdelete:
                del lstTbl[entry]
                print()
                
                
    # Save a formatted file to CDInventory.txt
    elif strChoice == 's':
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        
        
    # Notifies user if incorrect entry is entered
    else:
        print('Please choose either l, a, i, d, s or x!')
        print()



