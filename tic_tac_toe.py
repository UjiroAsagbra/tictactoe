from bts import draw_board, check_turn, check_for_win
import os

spots = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # RESET THE SCREEN
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #IF AN INVALID TURN OCCURS, LET PLAYER KNOW
    if prev_turn == turn:
        print('Invalid spot selected, please pick another.')
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) +"'s turn: Pick your spot or press q to quit")
    # GET INPUT FROM PLAYERS
    choice = input()
    if choice == 'q':
        playing = False
        #CHECKS IF THE PLAYER GAVE A NUMBER FROM 1 - 9
    elif str.isdigit(choice) and int(choice) in spots:
        #CHECK IF THE SPOT HAS BEEN TAKEN
        if not spots[int(choice)] in {'X' , 'O'}:
            #VALID INPUT, UPDATE THE BOARD
            turn += 1
            spots[int(choice)] = check_turn(turn)
    # CHECK IF THE GAME HAS ENDED AND IF SOMEONE WON
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#DECLARE WINNER
if complete:
    if check_turn(turn) == 'X': print('Player 1 Wins!!')
    else: print("Player 2 Wins!!")
else:
    print('No Winner')

print('Thanks for playing!')
