import os           #for clearing console
import random       #for some moves
import time         #for fade out screen

current = [" ", " ", " ", " ", " ", " ", " ", " ", " "] # List of current table status
player1 = True                                          #Wich turn
winLines= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #Win combinations
predictionos = [ 0,0,0,0, 0,0,0,0 ]                     #predictions where line will be
_defaultPositions = [0,1,2,3,4,5,6,7,8]                 #default list of positions
_center = 4                                             #center cell index
_corners= [0,2,6,8]                                     #corner cell indexes
victory = False                                         
tekko   = False
moveNum = 1

XWON="""
            ______                           /\    \                /::\    \                /\    \         
           |::|   |                         /::\    \              /::::\    \              /::\    \        
           |::|   |                         \:::\    \            /::::::\    \             \:: \    \        
           |::|   |                       ___\:::\    \          /::::::::\    \             \:::\    \      
           |::|   |                      /\   \:::\    \        /:::/~~\:::\    \             \:::\    \ 
           |::|   |                     /::\   \:::\    \      /:::/    \:::\    \             \:::\    \ 
           |::|   |                     \:::\   \:::\    \    /:::/    / \:::\    \             \:::\    \   
           |::|   |                   ___\:::\   \:::\    \  /:::/____/   \:::\____\             \:::\    \  
     ______|::|___|___ ____          /\   \:::\   \:::\    \|:::|    |     |:::|    |_____________\:::\    \ 
    |:::::::::::::::::|    |        /::\   \:::\   \:::\____|:::|____|     |:::|    /::::::::::::::\:::\____\ 
    |:::::::::::::::::|____|        \:::\   \:::\__/:::/    /\:::\    \   /:::/    /\::::::::::::::::::/    /
     ~~~~~~|::|~~~|~~~               \:::\   \::::::::/    /  \:::\    \ /:::/    /  \::::::::::::::::/____/ 
           |::|   |                   \:::\   \::::::/    /    \:::\    /:::/    /    \::::\   \  
           |::|   |                    \:::\   \::::/    /      \:::\__/:::/    /      \::::\   \   
           |::|   |                     \:::\__/:::/    /        \::::::::/    /        \::::\   \   
           |::|   |                      \::::::::/    /          \::::::/    /          \::::\   \      
           |::|   |                       \::::::/    /            \::::/    /            \::::\   \      
           |::|   |                        \::::/    /              \::/____/              \::::\___\       
           |::|___|                         \::/____/                ~~                     \::/    /        
            ~~                               ~~                                              \/____/    """     

OWON="""
            _______                           _____                  _______                  _____          
           /::\    \                         /\    \                /::\    \                /\    \         
          /::::\    \                       /::\    \              /::::\    \              /::\    \        
         /::::::\    \                      \:::\    \            /::::::\    \             \:: \    \        
        /::::::::\    \                   ___\:::\    \          /::::::::\    \             \:::\    \        
       /:::/~~\:::\    \                 /\   \:::\    \        /:::/~~\:::\    \             \:::\    \     
      /:::/    \:::\    \               /::\   \:::\    \      /:::/    \:::\    \             \:::\    \   
     /:::/    / \:::\    \              \:::\   \:::\    \    /:::/    / \:::\    \             \:::\    \   
    /:::/____/   \:::\____\           ___\:::\   \:::\    \  /:::/____/   \:::\____\             \:::\    \ 
   |:::|    |     |:::|    |         /\   \:::\   \:::\    \|:::|    |     |:::|    |_____________\:::\    \ 
   |:::|____|     |:::|    |        /::\   \:::\   \:::\____|:::|____|     |:::|    /::::::::::::::\:::\____\ 
    \:::\    \   /:::/    /         \:::\   \:::\__/:::/    /\:::\    \   /:::/    /\::::::::::::::::::/    /
     \:::\    \ /:::/    /           \:::\   \::::::::/    /  \:::\    \ /:::/    /  \::::::::::::::::/____/ 
      \:::\    /:::/    /             \:::\   \::::::/    /    \:::\    /:::/    /    \::::\   \  
       \:::\__/:::/    /               \:::\   \::::/    /      \:::\__/:::/    /      \::::\   \   
        \::::::::/    /                 \:::\__/:::/    /        \::::::::/    /        \::::\   \    
         \::::::/    /                   \::::::::/    /          \::::::/    /          \::::\   \      
          \::::/    /                     \::::::/    /            \::::/    /            \::::\   \      
           \::/____/                       \::::/    /              \::/____/              \::::\___\    
            ~~                              \::/____/                ~~                     \::/    /        
                                             ~~                                              \/____/  """ 

TEKKO="""

             /\    \                  /\    \               |\    \            |\    \               /::\    \        
            /::\____\                /::\____\              |:\____\           |:\____\             /::::\    \       
           /:::/    /               /:::/    /              |::|   |           |::|   |            /::::::\    \      
          /:::/    /               /:::/    /__       ___   |::|   |     ___   |::|   |           /::::::::\    \     
         /:::/    /               /:::/   /\   \     /\  \  |::|   |    /\  \  |::|   |          /:::/~~\:::\    \    
        /:::/____/               /:::/   /::\___\   /::\  \ |::|   |   /::\  \ |::|   |         /:::/    \:::\    \   
       /::::\    \              /:::/   /:::/  /    \:::\  \|::|   |   \:::\  \|::|   |        /:::/    / \:::\    \  
      /::::::\    \            /:::/   /:::/  /      \:::\  |::|___|____\:::\  |::|___|______ /:::/____/   \:::\____\ 
     /:::/\:::\    \          /:::/   /:::/  /  ___   \:::\/::::::::\    \ ::\/::::::::\    \|:::|    |     |:::|    |
    /:::/  \:::\    \        /:::/   /:::/  /  /\   \  \:::::::::::::\____\:::::::::::::\____|:::|____|     |:::|    |
    \::/    \:::\    \       \:::\  /:::/  /  /::\___\  \:::\   \          \:::\   \          \:::\    \   /:::/    / 
     \/____/ \:::\    \       \:::\/:::/  /  /:::/   /   \:::\   \          \:::\   \          \:::\    \ /:::/    /  
              \:::\    \       \::::::/  /  /:::/   /     \:::\   \          \:::\   \          \:::\    /:::/    /   
               \:::\    \       \::::/  /  /:::/   /       \:::\   \          \:::\   \          \:::\__/:::/    /    
                \:::\    \       \:::\ /  /:::/   /         \:::\___\          \:::\___\          \::::::::/    /     
                 \:::\____\       \:::\  /:::/   /           \::/   /           \::/   /           \::::::/    /      
                  \::/    /        \::::::::/   /             \/___/             \/___/             \::::/    /       
                   \/____/          \::::::/   /                                                     \::/____/       """                                                                                                                     

def newGame():                                   
    """reset all the varibles for new game"""
    global current,player1,victory,tekko,moveNum
    current = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1 = True
    victory = False
    tekko   = False
    moveNum = 1

def move(pos):
    """
    Table of the game:

        0 │ 1 │ 2           Function takes a position
       ───┼───┼───          validate it and checks
        3 │ 4 │ 5           if this position is free
       ───┼───┼───          add to it X or O
        6 │ 7 │ 8           and change to next player

       .
    """
    global player1,moveNum
    if pos in range(0,9) and current[pos]==" ":    #If in valid position and it is free
        current [pos] = 'X' if player1 else 'O'  #Put X or O to "current" list
        player1 = not player1                    #Change the player
        moveNum += 1
        return True
    else:
        return False

def checkForWinner():
    """
                
     Function checkForWinner takes no args                   
     It looks in "current" array and checks              
      if it have same symbols in indexes             
       that wrote in "winLines" array 
       Also if all the chart is full
       it defines "tekko" as True    
     returns sequens of winning symbols


             ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿
    """
    global victory, tekko
    
      
    for c in winLines:
        if current[c[0]] == current[c[1]] == current[c[2]]:
            if current[c[0]] != " ":
                victory = True
                return c
    
    tekko = True 
    for c in current:
        if c == " ":
            tekko = False
            return [0,1,2,3,4,5,6,7,8]
    
    return [0,1,2,3,4,5,6,7,8]

def veiwTable(full=False,pattern=[_defaultPositions]):
    """
        Just veiw the table of the game and a hint table

        Has two arguments full and pattern.
        - when full is True shows both tables when False just game table 
            equals to False on default
        - pattern is list of numbers that will be shown (just when full is False)
            equals to _defaultPositions on default
    """

    if full:
        print(f' {current[0]} │ {current[1]} │ {current[2]}\t 0 │ 1 │ 2')
        print("───┼───┼─── \t───┼───┼─── " )
        print(f' {current[3]} │ {current[4]} │ {current[5]}\t 3 │ 4 │ 5')
        print("───┼───┼─── \t───┼───┼─── ")
        print(f' {current[6]} │ {current[7]} │ {current[8]}\t 6 │ 7 │ 8')
        print()
    else:
        print("\033[1m" +f' {current[0]if 0 in pattern else " "} | {current[1]if 1 in pattern else " "} | {current[2]if 2 in pattern else " "}')
        print("───┼───┼─── " )
        print("\033[1m" +f' {current[3]if 3 in pattern else " "} | {current[4]if 4 in pattern else " "} | {current[5]if 5 in pattern else " "}')
        print("───┼───┼─── ")
        print("\033[1m" +f' {current[6]if 6 in pattern else " "} | {current[7]if 7 in pattern else " "} | {current[8]if 8 in pattern else " "}')
        print()

def isFree(*args):
    """
    Checking if 1 or sequense of indexes are free in "current" array
    and return True or False if free or not respectivly 
    """

    if len(args)>1:                 #if args is list
        for i in args:              #check each one
            if current[i]!=" ":     #if it not free
                return False        #return False

        return True                 #else return True

    elif len(args)==1:              #if args is one varible
        if current[args[0]]==" ":   #if it free
            return True             #return True
        else:
            return False            #else return False

def row(symbol):
    """
        this function checks what row can make "symbol"('X' or 'O')
        on the next move it checks all the win combinations and cheks
        if symbol fit in each combination, and add all the equalities 
        to "predictions" list than it picks biggest num (2) and return
        last position in "current" list

        Example :
                                
           │   │ O          indexes   0   1   2   3   4   5   6   7   8
        ───┼───┼───         current [" "," ","O"," ","X"," "," "," ","X"]
           │ X │            row('X') will check winList
        ───┼───┼───         it will find [0,4,8] pattern and check this indexes
           │   │ X          in current, then will return 0 index because it still blank

    """
    global predictionos
    opponent = symbol
    me = 'O' if symbol == 'X' else 'X'
    predictionos = [ 0,0,0,0, 0,0,0,0 ]

    for pos,com in enumerate(winLines):
        for i in com:
            if current[i] == opponent and predictionos[pos] != -1:
                predictionos[pos] += 1
            elif current[i] == me:
                predictionos[pos] = -1
    
    if(max(predictionos)==2):
        for i in winLines[predictionos.index(max(predictionos))]:
            if current[i] != opponent:
                return i
    else:
        return -1

def getMove():  
    """
        Function that checks posibilities of O and X
        and desides where to put O
        also catches the center cell if free
        returns position 0-8

    """

    if isFree(_center):
        return _center
    elif moveNum == 2:
        return random.choice(_corners)
    else:
        X = row('X')
        O = row('O')
        if X == -1 and O == -1:
            r = list()
            for i,sym in enumerate(current):
                if sym == " ":
                    r.append(i)
            return random.choice(r)
        if O == -1:
            return X
        else:
            return O   

def pvp():  
    """
       Player vs Player game
       resets all needed varibles
       taking input from users

    """
    newGame()
    os.system('cls||clear')
    while not victory and not tekko:
        veiwTable(True)

        pos = input('palce X (0-8): ' if player1 else 'palce O (0-8): ' )
        
        try:
            pos = int(pos)
        except :
            print("just numbers ")
        

        move(pos)
        checkForWinner()
        os.system('cls||clear')
    
    veiwTable(False,checkForWinner())
    print(TEKKO) if tekko else print(OWON if player1 else XWON)

def pve():
    """
        Player vs Envirement game
        resets all needed varibles 
        takes input from user
        and decides where to go

    """
    newGame()
    msg =''
    while not victory and not tekko:
        
        sucssess = False
        while not sucssess:
            os.system('cls||clear')
            veiwTable(True)
            print(msg,end=' ')
            pos = input('palce X to 0-8: ' if player1 else 'palce O (0-8): ' )
            
            try:
                pos = int(pos)
            except :
                msg ="just numbers "

            sucssess = move(pos)
        if checkForWinner()!=_defaultPositions:
            os.system('cls||clear')
            veiwTable(False,checkForWinner())
            print(TEKKO) if tekko else print(OWON if player1 else XWON)
            break
        
        sucssess = False
        if moveNum<9:
            while not sucssess:
                sucssess = move(getMove())
        
        checkForWinner()
        os.system('cls||clear')
        if checkForWinner()!=_defaultPositions:
            os.system('cls||clear')
            veiwTable(False,checkForWinner())
            print(TEKKO) if tekko else print(OWON if player1 else XWON)
            break


def main():
    """
        Main loop that takes your input 
        and brings you to pvp, pve, or exit
    """
    choice = 1
    while choice == 1 or choice == 2 or choice == 3 or choice == 4:
        os.system('cls||clear')
        
        if choice == 3:
            print("Just numbers please ")
        elif choice == 4:
            print("Wrong exit password (•ิ_•ิ)?")
        
        t = input("Enter: \n1 - for pve \n2 - for pvp\n5 digit password to exit \nYour choice : ")
        
        try:
            t = int(t)
        except :
            choice = 3


        if t == 1:
            pve()
            time.sleep(1)
        elif t == 2:
            pvp()
            time.sleep(1)
        elif 9999<t<100000:
            os.system('cls||clear')
            break
        else:    
            choice = 4
    
main() 
 