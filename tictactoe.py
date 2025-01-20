import random
#Variables
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
gamestart=True
gamemode=None
boton=False
currentletter= None
currentplayer= 1
playing = True
winnerfound= False
winner = None
gameover=None

#game start up
def startup():
    global boton
    global gamemode
    global currentplayer
    while not gamemode:
        print("Welcome to Tic-Tac-Toe please select a game mode \n 1-Against computer \n 2-Against player")
        option=int(input('1 or 2:'))
        currentplayer=1
        if option==(1):
            boton=True
            gamemode=True
        elif option==2:
            gamemode=True
        else:
            new_func()

def new_func():
    print("Invalid input please choose 1 or 2")
def letterchoice():
    global playing
    global currentletter
    global gamestart
    global gamemode
    if gamemode:
        print("Player 1 choose X or O")
    letter=input('X or O:')
    if letter=="X":
        currentletter= "X"
        gamestart=False
        gamemode=False
        playing= True
    elif letter=='O':
        currentletter= 'O'
        gamestart=False
        gamemode=False
        playing= True
    else:
        print("Invalide input please choose X or O")
def gamestartup():
    while gamestart:
        startup()
        letterchoice()

#computer
def computer(board):
    global currentletter
    while currentplayer==2 and boton:
        inpt=random.randint(0,8)
        if board[inpt]== " ":
            new_varnew_var = new_func1(board, inpt)
            
            turns()
            changeletter()
            

def new_func1(board, inpt):
    board[inpt]= currentletter
#printing the board
def visual(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])

#player input
def moves(board):
    inp = int(input('number from 1 to 9:'))
    if inp>= 1 and inp<=9 and board[inp-1]==' ':
        board[inp-1]=currentletter
    else:
        print('That spot is invalid please select another' )
#win conditions

def horizontalwin(board):
    global winner
    global winnerfound
    if board[0]==board[1]==board[2] and board[0]!=' ':
        winner=board[0]
        winnerfound=True
    elif board[3]==board[4]==board[5] and board[3]!=' ':
        winner=board[3]
        winnerfound=True
    elif board[6]==board[7]==board[8] and board[6]!= ' ':
        winner=board[6]
        winnerfound=True
def verticalwin(board):
   global winner
   global winnerfound
   if board[0]==board[3]==board[6] and board[6]!=' ':
        winner=board[0]
        winnerfound=True
   elif board[1]==board[4]==board[7] and board[4]!=' ':
        winner=board[3]
        winnerfound=True
   elif board[2]==board[5]==board[8] and board[8]!= ' ':
        winner=board[6]
        winnerfound=True
def tie(board):
   global playing
   if ' ' not in board and not winnerfound:
       visual(board)
       print('Tie! Everyone wins!')
       playing= False
def checkwin(board):
    global playing
    global winnerfound
    if winnerfound:
        print(f"The winner is {winner}")
        playing = False
        visual(board)
#Turn order
def turns():
    global currentplayer
    if currentplayer==1:
        currentplayer=2
    else:
        currentplayer=1
def changeletter():
    global currentletter
    if currentletter== "X":
        currentletter="O"
    elif currentletter=="O":
        currentletter= "X"
  
 #gameloop
def gameloop():
    while playing and not gamestart:
        computer(board)
        visual(board)
        moves(board)
        horizontalwin(board)
        verticalwin(board)
        checkwin(board)
        tie(board)
        turns()
        changeletter()
       
     


#restart
   
def restart(): 
    global gamestart
    global board
    global winnerfound
    global boton
    global playing
    global gameover
    while not playing and not gamestart and not gameover:
        print("Game over do you want to play again? 'Y/N'")
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        endgame=input('Y/N:')
        if endgame== "Y":
            gamestart= True
            winnerfound=False
            boton= False
        elif endgame=='N':
            gameover=True
            break
        else:
            break
def gamerestart():
    while not playing and not gamestart and not gameover:
        restart() 
    

while not gameover:
    gamestartup()
    gameloop()
    gamerestart()