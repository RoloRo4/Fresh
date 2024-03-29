import random

print('\n'*100)

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']



def display_board(board):
    
    print(board[7] + " --", board[8] + " --", board[9])
    print(board[4] + " --", board[5] + " --", board[6])
    print(board[1] + " --", board[2] + " --", board[3])


def player_input():
    
    marker = ""
    accept_values = ["X","O"]
    
    while marker not in accept_values:
        
        marker = input("Player 1, Please choose your marker (X or O)")
        if marker not in accept_values:
            print ("Incorrect, chose your marker again! Capitalization Matters!")
    
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
        
    return (player1, player2)


def place_marker(board, marker, position):
    
    board[position] = marker
    
    return board

def win_check(board, mark):
    
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


def choose_first():
    
    play1 = random.randint(0,100)
    play2 = random.randint(0,100)
    
    if play1 >= play2:
        return "Player 1"
    else:
        return "Player 2"



def space_check(board, position):
    
    if board[position] == " ":
        return True
    else:
        return False

def full_board_check(board):
    
    for x in range(1,10):
        
        if space_check(board, x):
            return False
    return True


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        
        position = int(input('Choose a position: (1-9)'))
        
    return position
    
        


def replay():
    
    print ("Would you like to play again?")
    values = ['Y', 'N']
    choice = ''
    
    while choice not in values:
        
        choice = input ("Y/N?")
        if choice not in values:
            print ("Please try again (Y/N)")
    
    if choice == "Y":
        return True
    else:
        return False
    
            
# While Loop To Keep Running The Game

print("Welcome to Tic Tac Toe!")


while True:
    
    game_board = [" "]*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input ('Ready to play? Y or N?')
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        
        
    while game_on:
        
        if turn == "Player 1":
            
            display_board(game_board)
            
            position = player_choice(game_board)
            
            place_marker(game_board, player1_marker, position)
            
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print('Player 1 has won!')
                game_on = False
                
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = "Player 2"
                    
        else:
            
            display_board(game_board)
            
            position = player_choice(game_board)
            
            place_marker(game_board, player2_marker, position)
            
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Player 2 has won!')
                game_on = False
                
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print("Tie game!")
                    game_on = False
                else:
                    turn = "Player 1"
                    
            
    if not replay():
        break
    

    
    


















