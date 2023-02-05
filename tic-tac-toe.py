#Tic-Tac-Toe 
#Sun Feb 5, 2023 16:25
from random import randint
board = [[1,2,3],[4,'x',6],[7,8,9]]
def display_board(board):
    for i in range(3):
        print('+','+','+','+',sep='-'*7)
        for j in range(3):
            print('|',' '*5,'|',' '*5,'|',' '*5,'|')
            if j < 1:
                print('|  ',board[i][j],' ','|  ',board[i][j+1],' ','|  ',board[i][j+2],' ','|')
                print('|',' '*5,'|',' '*5,'|',' '*5,'|')
                break
    print('+','+','+','+',sep='-'*7)

def user_move(board):
    move = True
    while move:
        user_move = int(input('Enter your move: '))
        if user_move > 0 and user_move < 10 :
            user_move-=1
            r = user_move//3
            c = user_move%3
            if board[r][c] not in ['0','x']:
                board[r][c]='0'
                move = False
            else:    
                print('Position already occupied')
                continue
        else:            
            print('Please enter only one position number(Which is not occupied) at a time, from 1 to 9')
            continue        
def ai_move(board):
    move = True
    while move:
        ai = randint(1,9)
        ai-=1
        r = ai//3
        c = ai%3  
        if board[r][c] not in ['0','x']:
            board[r][c]='x'
            move = False
        continue

def is_victory(sgn):
	for i in range(3):
		if board[i][0] == sgn and board[i][1] == sgn and board[i][2] == sgn:	#check every row
			return True
		if board[0][i] == sgn and board[1][i] == sgn and board[2][i] == sgn:    #check every column
			return True
	if board[0][0] == sgn and board[1][1] == sgn and board[2][2] == sgn:       #checks diagonally
			return True
	if board[0][2] == sgn and board[1][1] == sgn and board[2][0] == sgn:       #checks diagonally
			return True
	return False

def is_draw(board):        #checks if any spot is free                                                  
    x =[1,2,3,4,5,6,7,8,9]
    for i in range(3):
        for j in range(3):
            if board[i][j] in x:
                return False
    return True            
def game_on():
    while True: 
        display_board(board)
        user_move(board)
        if is_victory("0"):
            display_board(board)
            print("Yeah! We are goat.")
            break
        elif is_draw(board):
            display_board(board)
            print("Tie!")
            break
        ai_move(board)
        if is_victory("x"):
            display_board(board)
            print("Skynet Rules!!!")
            break
        elif is_draw(board):
            display_board(board)
            print("Tie!")
            break
game_on()        